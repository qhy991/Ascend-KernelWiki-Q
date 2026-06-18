---
id: kernel-paged-attention-npu
title: "AscendC Paged Attention — Block KV Cache for NPU Inference"
type: wiki-kernel
architectures: [ascend910b]
tags: [paged-attention, attention, flash-attention, ascendc, inference]
confidence: source-reported
kernel_types: [attention, flash-attention]
languages: [ascendc]
sources: [doc-vllm-ascend, pr-vllm-ascend-001, doc-ascendc-api-reference]
related: [kernel-flash-attention-npu, technique-kv-cache-paging, technique-online-softmax]
techniques: [cube-vector-overlap, online-softmax]
reproducibility: snippet
operator_recipe:
  operator: paged-attention
  dtype: [fp16, bf16]
  layout: [block-kv-cache, block-table, head-major]
  shape_class: [prefill, decode, long-sequence]
  memory_path:
    global_memory: [Q, K-cache-block-pool, V-cache-block-pool, block-table, output]
    onchip_buffers: [UB, L1, L0A, L0B, L0C]
    data_formats: [blocked-KV, contiguous-query-tile]
  parallelism:
    granularity: sequence head and KV block tiles
    block_dim: active attention tiles per batch/head
    sync_scope: per-query online-softmax state
  instruction_family: [Mmad, Vector-softmax]
  library_backend: [AscendC, vLLM-Ascend, CANN]
  tiling:
    tile_axes: [query, kv-block, head-dim]
    tile_granularity: fixed KV cache block plus query tile
    constraints: [block-table-indirection, head-dim-alignment, UB-capacity]
  pipeline:
    stages: [GatherKVBlock, QKMatmul, OnlineSoftmax, PVMatmul, NormalizeAndStore]
    queues: [MTE, Cube, Vector]
    overlap: next KV block DataCopy overlaps current score/softmax/value work
  aicore_mapping:
    block_dim: batch-head-query-block tiles
    scheduling: assign independent sequence/head/block tiles to AICores while preserving per-query softmax state
  data_movement:
    apis: [DataCopy]
    path: "block_table -> GM KV block -> UB/L1/L0 -> score/value tiles -> GM output"
  compute_path:
    units: [Cube Unit, Vector Unit]
    primitives: [Matmul, ReduceMax, Exp, ReduceSum, Mul, Add]
---

# AscendC Paged Attention — Block KV Cache for NPU Inference

Paged Attention adapts the vLLM PagedAttention scheme to the Ascend 910B NPU: the KV cache is stored as fixed-size blocks scattered across non-contiguous physical memory, and a per-sequence block table maps logical positions to physical blocks. The kernel gathers the K/V blocks for a sequence through its block table into the Unified Buffer, then runs online-softmax flash attention (`Q@K^T` on the Cube Unit, scale + softmax on the Vector Unit, `P@V` on the Cube Unit) without ever materializing the full score matrix. Compared with the contiguous-layout `kernel-flash-attention-npu`, the only structural change is an indirect, block-table-driven gather of K and V; the math and the Cube/Vector overlap are identical.

## Why Paging

LLM inference appends one token per decode step, so each sequence's KV cache grows unpredictably. Allocating a contiguous, max-length buffer per sequence wastes most of it. PagedAttention instead carves the cache into fixed-size blocks (commonly 16 or 128 tokens of K and V) and tracks, per sequence, which physical blocks hold which logical positions:

```
block_table[seq][blk] -> phys_block_id
```

Blocks are non-contiguous in physical (global) memory, allocated on demand from a shared pool. Because only the last block of a sequence is partially filled, internal fragmentation is bounded to one block per sequence — under 4% KV memory waste in practice (per `doc-vllm-ascend`). This is the storage half of the design; see `technique-kv-cache-paging` for the allocator and block-table mechanics. This page covers the compute half: the attention kernel that consumes the block table.

## Decode vs Prefill

The same kernel serves two regimes with different shapes:

| Phase   | Query tokens | KV source                              | Cube shape per block         |
|---------|--------------|----------------------------------------|------------------------------|
| Prefill | seqlen_q     | newly written blocks for this sequence | `seqlen_q × block × headdim` |
| Decode  | 1            | all cached KV blocks for the sequence  | `1 × block × headdim`        |

- **Prefill** processes the prompt in one shot. Multiple query tokens attend to the just-written KV blocks; this looks much like contiguous flash attention because the blocks were allocated together, but the gather path is still used for uniformity.
- **Decode** is the steady-state inner loop: a single query token attends to *all* cached KV blocks of its sequence, walked one block at a time through the block table. The query is a single row, so the `Q@K^T` GEMM degenerates to a matrix-vector product per block — Cube-Unit occupancy is low and the kernel becomes gather- and Vector-bound. This is the case the kernel must optimize hardest.

## Algorithm

Online softmax (running max `m_i`, running denominator `l_i`) lets the kernel fold each KV block into the output as soon as it is gathered, so the `seqlen_q × seqlen_k` score matrix never exists in full (see `technique-online-softmax`). For a query tile, walking blocks `j = 0..num_blocks`:

```
Initialize O = 0, m = -inf, l = 0
For each logical block j in block_table[seq]:
    phys = block_table[seq][j]
    K_blk, V_blk = gather(phys)              (MTE: indirect DataCopy from GM)
    S = Q @ K_blk^T                          (Cube Unit)
    m_new = max(m, rowmax(S))                (Vector Unit)
    P = exp(S - m_new)                        (Vector Unit)
    alpha = exp(m - m_new)                    (Vector Unit, rescale prev state)
    l = alpha * l + rowsum(P)                 (Vector Unit)
    O = alpha * O + P @ V_blk                 (Cube Unit)
    m = m_new
Output O / l
```

The rescale factor `alpha = exp(m_prev - m_new)` corrects the previously accumulated `O` and `l` whenever a new block raises the running max, which is what keeps the streaming sum numerically equivalent to a single global softmax.

## AscendC Implementation Sketch

The kernel differs from `kernel-flash-attention-npu` in exactly one place: K and V are not read with a contiguous base-plus-stride `DataCopy`. Instead, each iteration reads the next physical block id from the block table and issues a `DataCopy` from that block's global-memory address into the Unified Buffer.

```cpp
extern "C" __global__ __aicore__ void paged_attention_decode(
    __gm__ half* Q,              // [1, headdim]   single decode query
    __gm__ half* K_cache,        // block pool, [num_blocks, block, headdim]
    __gm__ half* V_cache,        // block pool, same layout as K_cache
    __gm__ int32_t* block_table, // [num_blocks_for_seq] -> phys block id
    __gm__ half* Output,         // [1, headdim]
    int num_blocks, int block, int headdim) {

    TPipe pipe;

    // Query stays resident in UB (reused across every KV block)
    auto Q_tile = AllocUB<half>(headdim);
    DataCopy(Q_tile, Q, {1, headdim});

    // Online-softmax accumulators (single query row)
    auto O_tile = AllocUB<half>(headdim);
    auto m_run  = AllocUB<half>(1);   // running max  m_i
    auto l_run  = AllocUB<half>(1);   // running sum  l_i
    Fill<half>(O_tile, 0.0, headdim);
    Fill<half>(m_run, -INFINITY, 1);
    Fill<half>(l_run, 0.0, 1);

    const int blk_elems = block * headdim;

    for (int j = 0; j < num_blocks; ++j) {
        // --- Block-table gather: indirect read of K/V block from the pool ---
        int32_t phys = block_table[j];
        auto K_blk = AllocUB<half>(blk_elems);
        auto V_blk = AllocUB<half>(blk_elems);
        DataCopy(K_blk, K_cache + (int64_t)phys * blk_elems, {block, headdim});
        DataCopy(V_blk, V_cache + (int64_t)phys * blk_elems, {block, headdim});

        // S = Q @ K_blk^T  (Cube Unit) -> [1, block]
        auto S = AllocUB<half>(block);
        Matmul(S, Q_tile, K_blk, {1, block, headdim});

        // m_new = max(m_run, rowmax(S))  (Vector Unit)
        auto block_max = AllocUB<half>(1);
        ReduceMax(S, block_max, {block}, 1);
        auto m_prev = AllocUB<half>(1);
        DataCopy(m_prev, m_run, 1);
        MaxElementwise(m_run, block_max, m_run, 1);

        // P = exp(S - m_new)  (Vector Unit)
        auto P = AllocUB<half>(block);
        Sub(S, m_run, S, block);
        Exp(S, P, block);

        // alpha = exp(m_prev - m_new); rescale running l and O
        auto alpha = AllocUB<half>(1);
        Sub(m_prev, m_run, alpha, 1);
        Exp(alpha, alpha, 1);

        // l = alpha * l + rowsum(P)
        auto sum_P = AllocUB<half>(1);
        ReduceSum(P, sum_P, {block}, 1);
        Mul(l_run, alpha, l_run, 1);
        Add(l_run, sum_P, l_run, 1);

        // O = alpha * O + P @ V_blk  (Cube Unit)
        auto PV = AllocUB<half>(headdim);
        Matmul(PV, P, V_blk, {1, headdim, block});
        Mul(O_tile, alpha, O_tile, headdim);
        Add(O_tile, PV, O_tile, headdim);
    }

    // Final normalization: O / l
    auto l_recip = AllocUB<half>(1);
    Reciprocal(l_run, l_recip, 1);
    Mul(O_tile, l_recip, O_tile, headdim);
    DataCopy(Output, O_tile, {1, headdim});
}
```

For prefill, `Q_tile` becomes a `[seqlen_q, headdim]` tile and the accumulators `m_run` / `l_run` are per-row vectors of length `seqlen_q`, exactly as in `kernel-flash-attention-npu`; only the K/V load path changes to the block-table gather shown above.

### Cube/Vector Overlap

As with contiguous flash attention, the kernel pipelines across blocks so the units stay busy (`technique-cube-vector-overlap`):

- **block j+1**: MTE gathers the next `K_blk` / `V_blk` from the pool, Cube computes `Q@K^T`.
- **block j**: Vector computes `rowmax`, `exp`, `rowsum`, and the `alpha` rescale.
- **block j-1**: Cube computes `P@V`.

The indirect gather adds an address-resolution step (read `block_table[j]`, compute the GM offset) ahead of each `DataCopy`, but the copy itself is a normal contiguous block transfer, so MTE bandwidth is unaffected once the address is known.

## Trade-offs and Pitfalls

**1. Gather-bound decode.** With a single query row, `Q@K^T` and `P@V` are matrix-vector products and the Cube Unit is underused. Throughput is limited by the rate of block gathers and Vector-Unit softmax, not by Cube FLOPs. Larger block sizes amortize the per-block address resolution and reduce DataCopy launch count.

**2. Block size vs fragmentation.** Small blocks keep KV memory waste under 4% but multiply the number of gather + Cube + Vector iterations per token. Large blocks improve Cube/MTE efficiency but raise the partial-block waste of the final block. The block size is a storage/compute trade-off owned by `technique-kv-cache-paging`.

**3. Non-contiguous addresses defeat prefetch.** Because consecutive logical blocks land at arbitrary physical offsets, the MTE cannot stride-prefetch K/V the way contiguous flash attention does. The block table must be resolved one entry ahead to hide gather latency behind compute.

**4. Online-softmax rescale must touch every accumulator.** A correctness pitfall: when a new block raises `m`, the `alpha = exp(m_prev - m_new)` factor must be applied to *both* `l` and the already-accumulated `O` before adding the new contribution. Rescaling only one of them silently corrupts the result (see `technique-online-softmax`).

**5. FP16 accumulation.** As in `kernel-matmul-ascendc`, the Cube Unit accumulates `Q@K^T` and `P@V` in FP32 internally; keep `exp` and the running `l` in a stable range to avoid overflow in long-context decode where `num_blocks` is large.

## Comparison with Contiguous Flash Attention

| Aspect            | kernel-flash-attention-npu        | kernel-paged-attention-npu               |
|-------------------|-----------------------------------|------------------------------------------|
| KV layout         | contiguous per sequence           | fixed blocks, non-contiguous in GM       |
| KV addressing     | base + stride                     | `block_table[seq][blk]` indirect gather  |
| KV memory waste   | up to max-length over-allocation  | bounded to last block (<4%)              |
| Softmax           | online (running `m`, `l`)         | online (running `m`, `l`)                |
| QK^T / PV         | Cube Unit                         | Cube Unit                                |
| Scale + softmax   | Vector Unit                       | Vector Unit                              |
| Decode efficiency | n/a (training/prefill oriented)   | gather/Vector-bound, low Cube occupancy  |

The takeaway: paging is a memory-layout change, not an algorithm change. The flash-attention math, the Cube/Vector split, and the online-softmax accumulators are shared verbatim with `kernel-flash-attention-npu`; paged attention simply inserts a block-table gather in front of every K/V load so the same kernel can run over a fragmented, dynamically allocated KV cache.
