---
id: hw-hccs
title: "HCCS — Huawei Cache Coherent System Interconnect"
type: wiki-hardware
architectures: [ascend910, ascend910b]
tags: [hccs, interconnect, communication, hardware]
confidence: source-reported
hardware_features: [hccs]
cuda_equivalent: nvlink
related: [technique-hccl-optimization, technique-tensor-parallel-overlap]
sources: [doc-hccl-collective, blog-ascend-910b-deep-dive]
---

# HCCS — Huawei Cache Coherent System Interconnect

HCCS (Huawei Cache Coherent System) is the high-bandwidth, cache-coherent interconnect that links Ascend NPUs to one another **inside a server node** — the direct analog of NVIDIA's NVLink. It is the physical fabric over which HCCL collectives (AllReduce, AllGather, ReduceScatter) move tensors during distributed training, and its bandwidth and topology directly determine how well tensor-parallel and data-parallel jobs scale. This page describes the on-server topology, the role HCCS plays for HCCL, and the topology-aware collective algorithms that ride on top of it.

## Why a Dedicated Interconnect

During distributed training, NPUs must exchange gradients, activations, and weight shards every step. If those exchanges went over PCIe to host memory and back, the interconnect would become the bottleneck long before the Cube units saturated. HCCS solves this by providing **direct NPU ↔ NPU links** that are:

- **Coherent** — peers can read each other's HBM with hardware-maintained coherence, avoiding host-staged copies.
- **High-bandwidth** — substantially faster than PCIe, so collective traffic does not stall compute.
- **Low-latency** — short on-board links keep small-message latency low, which matters for latency-bound AllReduce on small tensors.

## On-Server Topology

A typical Ascend training server packs multiple NPUs (commonly 8) that are wired together by HCCS. Across server boundaries, a separate fabric — **HCCN**, running RoCE (RDMA over Converged Ethernet) — carries traffic between nodes.

```
┌──────────────────────────── Node A ────────────────────────────┐
│   NPU0 ── HCCS ── NPU1 ── HCCS ── NPU2 ── HCCS ── NPU3          │
│    │ \             │                 │             / │          │
│  HCCS  ── ── ── full/partial mesh ── ── ── ── ── HCCS           │
│    │ /             │                 │             \ │          │
│   NPU4 ── HCCS ── NPU5 ── HCCS ── NPU6 ── HCCS ── NPU7          │
└─────────────────────────────────┬───────────────────────────────┘
                                   │  HCCN / RoCE (inter-node)
┌─────────────────────────────────┴───────────────────────────────┐
│                            Node B (NPU0..7)                       │
└──────────────────────────────────────────────────────────────────┘
```

Two interconnect tiers therefore exist, and HCCL chooses algorithms that respect the boundary between them:

| Tier | Fabric | Scope | Protocol | Relative bandwidth |
|------|--------|-------|----------|--------------------|
| Intra-node | **HCCS** | NPU ↔ NPU in one server | Coherent NPU links | Highest |
| Inter-node | **HCCN** | server ↔ server | RoCE (RDMA over Ethernet) | Lower than HCCS |
| Host path | PCIe | NPU ↔ host CPU/DRAM | PCIe | Lowest of the three |

The qualitative ordering — **HCCS > HCCN > PCIe** — is the single most important fact for collective design: every algorithm tries to maximize traffic on HCCS and minimize the bytes that must cross HCCN or PCIe.

## Carrying HCCL Collectives

HCCL (Huawei Collective Communication Library) is the CANN library that implements the collective primitives used by distributed frameworks. HCCS is the intra-node transport beneath these primitives. The core operations are:

- **AllReduce** — sum (or other reduction) a tensor across all ranks, result broadcast to all. The workhorse of data-parallel gradient synchronization.
- **AllGather** — concatenate each rank's shard so every rank holds the full tensor. Common in tensor-parallel weight gathering.
- **ReduceScatter** — reduce across ranks, then scatter disjoint slices to each rank. The reduce half of a Ring-AllReduce decomposition.

A minimal HCCL usage sketch (C, the library's native API surface):

```c
#include "hccl/hccl.h"

HcclComm comm;
// Build a communicator over `rankNum` NPUs sharing a rootInfo.
HcclCommInitRootInfo(rankNum, &rootInfo, rank, &comm);

// AllReduce a gradient buffer in-place across the HCCS-linked NPUs.
HcclAllReduce(
    sendBuf, recvBuf,
    count, HCCL_DATA_TYPE_FP16,
    HCCL_REDUCE_SUM,
    comm, stream);

// AllGather weight shards for tensor parallelism.
HcclAllGather(sendBuf, recvBuf, sendCount,
              HCCL_DATA_TYPE_FP16, comm, stream);

// ReduceScatter — the reduce phase of a ring AllReduce.
HcclReduceScatter(sendBuf, recvBuf, recvCount,
                  HCCL_DATA_TYPE_FP16, HCCL_REDUCE_SUM,
                  comm, stream);

HcclCommDestroy(comm);
```

These calls are enqueued on an aclrtStream and run asynchronously, which is what makes communication/compute overlap possible — see `technique-tensor-parallel-overlap`. The actual wire transport (which links are traversed, in what order) is selected internally by HCCL based on the discovered topology; the caller does not name HCCS explicitly. See `doc-hccl-collective` for the full primitive set and reduction operators.

## Topology-Aware Collective Algorithms

HCCL inspects the physical layout — how many NPUs share HCCS, how they are meshed, and where the HCCN boundary lies — and picks a collective algorithm that keeps the heavy traffic on the fastest links. The two dominant intra-node families are **ring** and **mesh**.

### Ring

Ranks are arranged in a logical ring; each rank sends to its successor and receives from its predecessor in lockstep steps. Ring-AllReduce is bandwidth-optimal: every link carries roughly `2(N-1)/N` of the data volume, and no link is a hotspot.

```
NPU0 → NPU1 → NPU2 → NPU3
  ↑                     │
  └─────────────────────┘   (wraps around)
```

- **Strength**: bandwidth-optimal, links evenly loaded — ideal for **large** tensors where bandwidth dominates.
- **Weakness**: latency scales with ring length (`N-1` steps), so it is poor for **small**, latency-bound messages.

### Mesh

When HCCS provides direct point-to-point links between (most) NPU pairs, a mesh/all-pairs schedule lets ranks exchange in fewer hops, trading some link-balance for lower latency.

- **Strength**: fewer steps → lower latency, good for **small** tensors and richly-connected fabrics.
- **Weakness**: can create link contention and is sensitive to whether the HCCS mesh is full or partial.

HCCL effectively switches between these based on message size and connectivity:

| Regime | Tensor size | Bound by | Algorithm HCCL tends to choose |
|--------|-------------|----------|--------------------------------|
| Large messages | big gradients | bandwidth | Ring (or ring-of-rings across nodes) |
| Small messages | tiny tensors | latency | Mesh / direct exchange |
| Multi-node | spans HCCN | both tiers | Hierarchical: HCCS ring within node, HCCN ring across nodes |

The hierarchical case is the key topology-aware win: reduce **within** each node over HCCS first, exchange only the partial results **across** nodes over the slower HCCN, then broadcast back inside each node. This minimizes the bytes that ever touch the slow fabric. Tuning these choices — and the buffering/overlap around them — is the subject of `technique-hccl-optimization`.

## Role in Parallel Scaling

HCCS underpins both major parallelism strategies:

- **Data parallelism** — each step ends in an AllReduce of gradients across replicas; HCCS bandwidth caps how large a model can sync per step without stalling.
- **Tensor parallelism** — a single layer's matmul is split across NPUs, requiring AllGather/ReduceScatter of activation/weight shards *inside* the forward and backward passes. Because these collectives sit on the critical path, overlapping them with Cube/Vector compute is essential; this is exactly what `technique-tensor-parallel-overlap` addresses by launching HCCL collectives on a separate stream while the AICores keep computing.

## Comparison with NVIDIA Fabrics

| Huawei Ascend | NVIDIA | Scope | Notes |
|---------------|--------|-------|-------|
| **HCCS** | **NVLink** | intra-node NPU/GPU links | Coherent, high-BW direct links |
| **HCCN (RoCE)** | **InfiniBand / RoCE** | inter-node | RDMA over the network fabric |
| **HCCL** | **NCCL** | collective library | AllReduce/AllGather/ReduceScatter |
| PCIe | PCIe | host ↔ accelerator | Slowest tier on both platforms |

The mental model maps cleanly: **HCCS is to Ascend what NVLink is to a GPU server**, and **HCCN/RoCE is the InfiniBand/RoCE-equivalent step-up-a-tier** to span nodes. Code-level equivalence is just as direct — an `HcclAllReduce` call corresponds to `ncclAllReduce`, with the same ring/tree-style topology awareness underneath.

## Trade-offs, Pitfalls, and Notes

1. **Respect the tier boundary.** A flat (non-hierarchical) collective that ignores the HCCS/HCCN split forces unnecessary bytes onto RoCE and can collapse multi-node throughput. Let HCCL build hierarchical schedules.
2. **Algorithm depends on message size.** Forcing ring for tiny tensors adds latency; forcing mesh for huge tensors creates link contention. Size-adaptive selection (and HCCL's own heuristics) matter — see `technique-hccl-optimization`.
3. **Overlap is not free.** Collectives only hide behind compute if launched on a separate stream *and* if there is enough independent compute to cover them; otherwise communication re-enters the critical path. See `technique-tensor-parallel-overlap`.
4. **Topology discovery matters.** Mis-mapped ranks (e.g., two ranks that frameworks place "adjacent" but that actually sit on opposite ends of a partial mesh) degrade ring efficiency. Pin ranks to NPUs that are well-connected over HCCS.
5. **PCIe is the fallback, not the path.** If HCCS peer access is unavailable or disabled, transfers silently fall back through host PCIe and tank performance; verify peer links are active.
6. **Confidence.** Bandwidth/latency claims here are *qualitative orderings* (HCCS > HCCN > PCIe) reported by sources, not measured numbers — consistent with this page's `source-reported` confidence. No specific GB/s figures are asserted.

## Best Practices

1. **Keep heavy traffic on HCCS** — design sharding so the largest collectives stay intra-node.
2. **Use hierarchical collectives** across nodes — reduce on HCCS first, cross HCCN with partials only.
3. **Overlap collectives with compute** — issue HCCL on a dedicated stream during tensor-parallel layers.
4. **Let HCCL pick ring vs mesh** — trust size-adaptive selection unless profiling shows a specific win.
5. **Validate rank placement** — ensure logically-adjacent ranks are physically well-connected on the HCCS mesh.
