---
id: hw-scalar-unit
title: "Scalar Unit — Control Flow and Address Generation"
type: wiki-hardware
architectures: [ascend910, ascend910b, ascend310p]
tags: [scalar-unit, control, hardware]
confidence: source-reported
hardware_features: [scalar-unit, instruction-queue]
related: [hw-cube-unit, hw-vector-unit, hw-instruction-queue]
sources: [doc-cann-architecture-guide, blog-ascend-910b-deep-dive]
---

# Scalar Unit — Control Flow and Address Generation

The Scalar Unit is the control processor of each AICore. It runs the kernel's control flow — loop counters, branch decisions, and pointer/offset arithmetic — and it is the component that issues instructions into the Cube, Vector, and MTE queues while managing the synchronization events that tie those queues together. Unlike a GPU, there is no warp scheduler in front of the compute engines: the Scalar Unit alone drives a single AICore.

## Core Functionality

The Scalar Unit handles everything that is *not* bulk SIMD compute or matrix multiply. It is responsible for four broad categories of work:

**Control flow**:
- Loop counters and trip-count management for tiling loops
- Branch decisions (`if`/`else`, early exit, boundary handling)
- Conditional dispatch of compute or transfer instructions

**Address and offset computation**:
- Computing global-memory (GM) offsets from the per-core block index
- Tile pointer arithmetic for staging data into the Unified Buffer (UB)
- Stride and padding math for non-contiguous accesses

**Instruction dispatch**:
- Issues instructions to the **Cube queue**, **Vector queue**, and **MTE queue**
- Issues its own scalar instructions on the **Scalar queue**
- See `hw-instruction-queue` for the full 4-queue model

**Synchronization**:
- Sets and waits on events that order operations across the four queues
- Inserts pipeline barriers where dependencies require it

## Role in the AICore

Each AICore has exactly **one Scalar Unit**. It is the front-end that keeps the heavy engines fed: the Cube Unit (`hw-cube-unit`) and Vector Unit (`hw-vector-unit`) only ever execute work that the Scalar Unit has dispatched into their respective queues. If the Scalar Unit is busy computing addresses or resolving branches, it cannot issue new compute instructions, and the compute queues drain.

```
        ┌──────────────────────────────────────────────┐
        │                 AICore                        │
        │                                               │
        │   ┌───────────────┐                           │
        │   │  Scalar Unit  │  control flow + address    │
        │   │  (1 per core) │  math + event sync         │
        │   └───────┬───────┘                           │
        │           │ issues instructions               │
        │   ┌───────┼───────────────┬──────────────┐    │
        │   ▼       ▼               ▼              ▼    │
        │  Scalar  Cube           Vector          MTE   │
        │  Queue   Queue          Queue           Queue │
        └──────────────────────────────────────────────┘
```

## Address Generation with the Block Index

The most common Scalar Unit task in an AscendC kernel is turning the per-core block index into a GM offset. `GetBlockIdx()` returns the index of the current AICore within the launch grid; the kernel multiplies it by the per-core tile size to find where in global memory this core's data lives.

```cpp
// Scalar Unit work: derive this core's GM offset from its block index
uint32_t blockIdx = GetBlockIdx();          // which AICore am I?
uint64_t coreOffset = blockIdx * tileLen;   // scalar address math

// Bind a GlobalTensor to the computed offset
GlobalTensor<half> xGm;
xGm.SetGlobalBuffer((__gm__ half*)x + coreOffset, tileLen);

// The Scalar Unit issues an MTE-queue transfer for this tile
DataCopy(xUb, xGm, tileLen);                // dispatched to MTE queue
```

Here the Scalar Unit computes `coreOffset`, binds the pointer with `SetGlobalBuffer`, and then dispatches the `DataCopy` into the MTE queue. The actual byte movement runs asynchronously on MTE; the Scalar Unit is free to compute the next offset.

## Contrast with the GPU SIMT Front-End

There is no direct CUDA equivalent to the Scalar Unit, which is why this page declares no `cuda_equivalent`. On an NVIDIA GPU, a hardware warp scheduler interleaves many warps to hide latency, and per-thread control flow (including divergence) is resolved by the SIMT engine. Ascend has no warp scheduler: a single Scalar Unit sequentially drives one AICore and explicitly hands work to the compute/transfer queues.

| Aspect | Ascend Scalar Unit | GPU SIMT Front-End |
|--------|--------------------|--------------------|
| Instances per core | One per AICore | One warp scheduler per SM |
| Latency hiding | Explicit queue overlap (MTE/Cube/Vector) | Implicit via warp interleaving |
| Control flow | Scalar-driven, single stream | Per-warp; divergence serializes lanes |
| Address generation | Explicit scalar math (`GetBlockIdx`) | Per-thread index registers |
| Programming model | Queue-aware, dispatch-explicit | SIMT, thread-implicit |

The practical consequence: latency that a GPU would hide by switching warps must instead be hidden on Ascend by overlapping the four queues — and that overlap only happens if the Scalar Unit can keep issuing.

## When the Scalar Unit Becomes the Bottleneck

Because one Scalar Unit feeds all the compute queues, it becomes a serial bottleneck whenever address computation or branching dominates the instruction stream. Symptoms reported in architecture write-ups include Cube and Vector queues sitting idle while the Scalar queue stays busy — the engines are *starved* because no new compute instruction has been issued.

Typical causes:
- **Complex indexing**: multi-dimensional stride math recomputed inside the inner loop
- **Branchy code**: per-tile boundary handling, ragged shapes, data-dependent branches
- **Fine-grained tiling**: many tiny tiles means the per-tile scalar overhead is paid more often, with little compute to amortize it
- **Repeated offset recomputation**: deriving the same base addresses every iteration instead of once

## Optimization Tips

**Precompute offsets outside the loop**:

```cpp
// Bad: recompute the base offset every iteration (Scalar Unit churns)
for (uint32_t i = 0; i < loopCount; i++) {
    uint64_t off = GetBlockIdx() * totalLen + i * tileLen;  // redundant
    DataCopy(ub, xGm[off], tileLen);
}

// Better: compute the invariant base once, then advance by a stride
uint64_t base = GetBlockIdx() * totalLen;                   // once
for (uint32_t i = 0; i < loopCount; i++) {
    DataCopy(ub, xGm[base + i * tileLen], tileLen);         // cheap add
}
```

**Minimize divergence**: hoist boundary handling (the "tail" tile) out of the main loop so the hot path is branch-free, and the Scalar Unit issues compute instructions back-to-back.

**Coarsen tiles**: larger tiles mean fewer loop iterations and fewer per-tile address computations, giving the Cube/Vector queues more work per dispatch to hide scalar overhead.

**Let the queues run**: avoid inserting `SyncAll`/`PipeBarrier` where a per-event sync would do; over-synchronizing forces the Scalar Unit to stall and prevents the overlap described in `hw-instruction-queue`.

## Trade-offs and Pitfalls

| Pattern | Effect on Scalar Unit | Effect on compute queues |
|---------|-----------------------|--------------------------|
| Precomputed, loop-invariant offsets | Lower scalar load | Higher utilization |
| Recomputing strides each iteration | Higher scalar load | Starvation risk |
| Branch-free hot path + separate tail | Lower divergence cost | Steady issue rate |
| Many tiny tiles | Per-tile overhead dominates | Frequent idle gaps |

**Notes and caveats**:
- The figures here are qualitative; this page is `source-reported`, and no benchmark numbers are claimed beyond the grounding.
- Scalar bottlenecking is workload-dependent. A compute-heavy GEMM with simple indexing rarely sees it; a kernel with ragged shapes or data-dependent control flow is far more exposed.
- The Scalar Unit's role is inseparable from the queue model — read `hw-instruction-queue` for how the four queues overlap, and `hw-cube-unit` / `hw-vector-unit` for the engines the Scalar Unit feeds.

The Scalar Unit is easy to overlook because it does no bulk arithmetic, but it is the issue engine for the entire AICore. Keeping its work light — precomputed offsets, minimal divergence, coarse enough tiles — is often what separates a kernel that saturates the Cube and Vector units from one that leaves them idle.
