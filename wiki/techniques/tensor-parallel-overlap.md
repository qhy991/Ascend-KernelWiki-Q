---
id: technique-tensor-parallel-overlap
title: "Tensor Parallelism — Communication/Compute Overlap with HCCL"
type: wiki-technique
architectures: [ascend910b]
tags: [tensor-parallel-overlap, hccl, communication, optimization]
confidence: source-reported
techniques: [tensor-parallel-overlap, hccl-optimization]
hardware_features: [hccs, cube-unit, global-memory]
kernel_types: [matmul, gemm, moe]
related: [technique-hccl-optimization, wiki-hardware-hccs, kernel-grouped-gemm-ascendc]
sources: [doc-hccl-collective, blog-ascend-910b-deep-dive]
reproducibility: concept
---

# Tensor Parallelism — Communication/Compute Overlap with HCCL

Tensor parallelism (TP) splits the weight matrices of a transformer layer across multiple NPUs so that each device computes a partial result, then exchanges results via an HCCL collective. On Ascend 910B the collective traverses the HCCS interconnect, and for large layers this AllReduce can become a significant fraction of step time. Overlapping that communication with the matmul that produces it is the key technique for restoring scaling efficiency.

## Megatron-Style Tensor Parallel Splitting

A standard transformer MLP/attention block is split using the two-GEMM Megatron pattern so that exactly one collective is required per block:

### Column-Parallel Linear (first GEMM)

The first weight `W1` of shape `[K, N]` is partitioned along its **output** dimension `N` into `tp` shards, one per device. Each NPU holds `W1_i` of shape `[K, N/tp]` and computes `Y_i = X @ W1_i` independently. No communication is needed because every device already has the full activation `X` (the input is replicated). The output is naturally sharded along `N`.

### Row-Parallel Linear (second GEMM)

The second weight `W2` of shape `[N, K]` is partitioned along its **input** dimension `N`, matching the sharding produced by the column-parallel GEMM. Each NPU computes a partial product `Z_i = Y_i @ W2_i` over its slice of the contraction dimension. Because each device only contracted over `N/tp` of the inner dimension, the partial sums must be reduced:

```
Z = sum_over_devices(Z_i)   # AllReduce over the TP group
```

This is the **AllReduce after the row-parallel GEMM**. By construction it is the only collective in the block: the column-parallel GEMM emits a sharded result that feeds directly into the row-parallel GEMM, so no intermediate communication occurs. For attention, the QKV projection is column-parallel and the output projection is row-parallel, following the same structure.

## Communication Cost over HCCS

The row-parallel AllReduce moves the full activation tensor `[M, K]` across the TP group. For a ring AllReduce over `tp` devices, each device sends and receives roughly `2 * (tp - 1) / tp * bytes(M, K)` of data, bounded by HCCS link bandwidth. Two consequences follow:

- The cost grows with sequence/batch size `M` and hidden size `K`, independent of how `N` was split.
- As `tp` grows, the per-link traffic approaches `2 * bytes(M, K)`, so the collective does not get cheaper with more devices — it is bandwidth-bound on HCCS. See `technique-hccl-optimization` for topology-aware algorithm selection (ring vs. hierarchical) and `hw-hccs` for the interconnect characteristics.

If this AllReduce runs serially after the GEMM, the NPU's Cube unit sits idle for the entire collective. The overlap strategies below hide that latency behind compute.

## Overlap Strategy 1 — Tile N and Pipeline the Collective

The row-parallel GEMM produces its output incrementally as it sweeps the `N` (here, the sharded contraction) and `M` dimensions. The idea is to **tile the matmul along the output `M`/row blocks** so that completed tiles can begin their AllReduce while later tiles are still computing on the Cube unit.

```cpp
// Conceptual: pipeline AllReduce of finished row-blocks with remaining compute.
// Each row-block of the partial output Z_i is reduced as soon as it is ready,
// while the Cube unit advances to the next block.
HcclComm comm;                       // TP-group communicator (from HcclCommInitRootInfo)
aclrtStream computeStream, commStream;

for (int blk = 0; blk < numBlocks; ++blk) {
    // 1. Cube unit computes partial product for this row-block: Z_i[blk] = Y_i[blk] @ W2_i
    MatmulBlock(Y_i, W2_i, Z_partial, blk, computeStream);

    // 2. As soon as the block is in GM, kick off its AllReduce on the comm stream.
    //    This runs concurrently with MatmulBlock(blk+1) on computeStream.
    aclrtSynchronizeStream(computeStream);   // ensure Z_partial[blk] is committed to GM
    HcclAllReduce(Z_partial + blk * blockBytes,
                  Z_out + blk * blockBytes,
                  blockElems, HCCL_DATA_TYPE_FP16,
                  HCCL_REDUCE_SUM, comm, commStream);
}
aclrtSynchronizeStream(commStream);          // drain the trailing collective
```

The pattern uses **two streams**: `computeStream` drives the Cube-unit GEMM blocks and `commStream` drives the `HcclAllReduce` calls. With `numBlocks` blocks, only the first GEMM block and the last AllReduce are unhidden; the steady-state interior is fully overlapped. The same two-stream async pattern is described in `technique-hccl-optimization`.

Practical guidance for choosing the tile:

- Blocks must be large enough that each `HcclAllReduce` amortizes the fixed collective launch overhead — too many tiny collectives is worse than one big one.
- Blocks must be small enough that several fit in the pipeline so compute can stay ahead of communication.
- Activations live in `global-memory` (GM); the producing GEMM must commit a block to GM before its collective reads it, hence the per-block stream synchronization.

## Overlap Strategy 2 — Fused Matmul + Collective

Rather than orchestrate the pipeline at the framework level, CANN exposes **fused communication-compute operators** that internalize the tiling and overlap. Two relevant fusions for the row-parallel GEMM are:

- **MatmulAllReduce** — fuses `Y_i @ W2_i` with the trailing AllReduce. The operator tiles the GEMM internally and issues the collective on completed tiles, so the AllReduce of early tiles overlaps the Cube computation of later tiles without the host driving two streams.
- **MatmulReduceScatter** — fuses the GEMM with a ReduceScatter instead of an AllReduce. This is the right primitive when the consumer of the output is itself sharded (e.g., a following sequence-parallel region), turning the `AllReduce` into the cheaper `ReduceScatter` + downstream `AllGather` split.

```cpp
// Conceptual: a single fused op replaces the manual two-stream loop.
// The kernel tiles internally and overlaps HCCS traffic with Cube compute.
MatmulAllReduce(/*a=*/Y_i, /*b=*/W2_i, /*out=*/Z_out,
                /*comm=*/comm, /*reduceOp=*/HCCL_REDUCE_SUM,
                /*stream=*/computeStream);
// For sequence-parallel consumers, use the ReduceScatter variant instead:
// MatmulReduceScatter(Y_i, W2_i, Z_scattered, comm, HCCL_REDUCE_SUM, computeStream);
```

Fusion removes the host round-trips and per-block synchronization of Strategy 1, and lets the kernel pick tile sizes from the GEMM tiling it is already computing.

## Application to MoE Grouped GEMM

In a Mixture-of-Experts layer the expert FFNs are evaluated as a grouped (batched) GEMM — see `kernel-grouped-gemm-ascendc`. With expert parallelism the tokens are routed via AllToAll, but when experts themselves are tensor-parallel the per-expert row-parallel GEMM still ends in an AllReduce over the TP sub-group. The same tile-and-pipeline or `MatmulReduceScatter` fusion applies per expert group, which matters because MoE blocks are communication-heavy and the grouped GEMM offers many independent tiles to hide the collective behind.

## Trade-offs, Pitfalls, and Notes

| Approach | Overlap | Host overhead | Flexibility | When to use |
|----------|---------|---------------|-------------|-------------|
| Serial GEMM then AllReduce | none | low | high | baseline / debugging |
| Strategy 1: tile N + two streams | good | higher (per-block sync) | high | framework-level control, custom tiling |
| Strategy 2: MatmulAllReduce | best | low | low | standard row-parallel linear |
| Strategy 2: MatmulReduceScatter | best | low | low | sequence-parallel downstream |

Pitfalls to watch:

1. **Block too small.** Each `HcclAllReduce` carries fixed launch cost; over-tiling along `N` floods HCCS with tiny collectives and regresses below the serial baseline. Tune block count against the cost model in `technique-hccl-optimization`.
2. **Missing GM commit.** A block's collective must not start before the GEMM has written that block to `global-memory`. Omitting the producer→consumer synchronization yields silently wrong reductions.
3. **Stream contention.** Compute and communication share the device; if the GEMM saturates HBM bandwidth, the concurrent AllReduce may not fully hide. Overlap helps most when the GEMM is Cube-bound rather than memory-bound.
4. **Topology mismatch.** Overlap reduces *exposed* latency but not *total* HCCS traffic. On undersized or non-ring topologies the collective can still dominate; algorithm selection (`hw-hccs`, `technique-hccl-optimization`) is the complementary lever.
5. **AllReduce vs. ReduceScatter.** If the downstream region is sequence-parallel, prefer `MatmulReduceScatter` — emitting a full AllReduce only to re-shard immediately wastes HCCS bandwidth.

This page describes the technique at the **concept** level. The TP split and the post-row-parallel AllReduce are well-established (source-reported, Megatron-style); the specific Ascend fused operators (`MatmulAllReduce`, `MatmulReduceScatter`) and HCCL APIs are named from CANN/HCCL references in `doc-hccl-collective` and the 910B analysis in `blog-ascend-910b-deep-dive`. No measured speedups are claimed here.
