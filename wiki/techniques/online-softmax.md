---
id: technique-online-softmax
title: "Online Softmax — Numerically Stable Streaming Softmax for Flash Attention"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [online-softmax, softmax, attention, flash-attention, optimization]
confidence: source-reported
techniques: [online-softmax]
hardware_features: [vector-unit, unified-buffer]
kernel_types: [softmax, flash-attention, attention]
related: [kernel-flash-attention-npu, kernel-softmax-ascendc, kernel-paged-attention-npu]
sources: [doc-ascendc-api-reference, blog-ascendc-performance-tips]
reproducibility: snippet
---

# Online Softmax for Streaming Flash Attention

Online softmax computes the softmax normalization incrementally as score blocks stream in, rather than waiting for the full attention score matrix to be available. By carrying a small set of running statistics — a row maximum, a row denominator, and the partially-accumulated output — it lets a flash attention kernel process attention one key/value block at a time, never materializing the `O(seq²)` score matrix in the Unified Buffer. This is the algorithmic core that makes `kernel-flash-attention-npu` and `kernel-paged-attention-npu` both memory-light and numerically stable.

## The Problem with Naive Softmax

The classic softmax for one query row over a length-`N` key dimension is `softmax(s)_j = exp(s_j) / Σ_k exp(s_k)`. A direct flash-attention implementation would:

1. Compute all `N` scores `s = Q·Kᵀ` and hold them in the Unified Buffer.
2. Take the global max, subtract, exponentiate, sum, divide.
3. Multiply the normalized probabilities by `V`.

This needs the full score row (and for batched rows, the full `S × S` matrix) resident at once. For long sequences that exceeds Unified Buffer capacity and forces spills to global memory. Online softmax removes that requirement by fusing the reduction with the streaming loop over key/value blocks.

## Running Statistics

Process the key/value dimension in blocks. For each query row keep three running quantities, indexed by the block step `i`:

- `m_i` — running row maximum of all scores seen so far
- `l_i` — running denominator (sum of rescaled exponentials)
- `O_i` — running unnormalized output accumulator

For block `i` with scores `s_ij = Q·Kⱼᵀ` and values `v_j`, the update is:

```
m_i = max(m_{i-1}, max_j s_ij)
α   = exp(m_{i-1} - m_i)                         # correction factor
l_i = l_{i-1} · α + Σ_j exp(s_ij - m_i)
O_i = O_{i-1} · α + Σ_j exp(s_ij - m_i) · v_j
```

After the final block, the normalized attention output for the row is `O_N / l_N`. The trick is the **correction factor** `α = exp(m_{i-1} - m_i)`: when a new block raises the running max, every previously-accumulated term was exponentiated against a stale (smaller) max, so it must be down-scaled by `α` to put `l` and `O` on the same footing as the freshly-computed terms. Because `m_i ≥ m_{i-1}`, `α ∈ (0, 1]` and the rescale never amplifies.

### Why It Is Numerically Stable

Every exponential argument is `s_ij - m_i ≤ 0`, so `exp(·) ∈ (0, 1]` and never overflows in fp16/fp32. Subtracting the running max is the streaming analogue of the standard "subtract the global max" stabilization in `kernel-softmax-ascendc`; the running max only ever increases, so the property `s_ij - m_i ≤ 0` is preserved at every step. The final ratio `O_N / l_N` is mathematically identical to the one-pass softmax — the running max cancels — so accuracy matches the naive form to floating-point rounding.

### Why It Is Memory-Light

The kernel only ever holds one score block (`O(block)`), the value block, and the per-row statistics (`m`, `l`, plus the `O` accumulator of head-dim width). It never stores the `O(seq²)` score matrix. This is what lets flash attention scale to long contexts within the Unified Buffer, and it is the same mechanism `kernel-paged-attention-npu` uses to fold paged KV-cache blocks into one running result.

## AscendC Implementation

The per-block update lives entirely on the **Vector unit** and uses the standard AscendC vector primitives — `ReduceMax`, `Sub`, `Exp`, `ReduceSum`, and `Mul` for the rescale. The score block `Q·Kⱼᵀ` is produced on the Cube unit beforehand (see `kernel-flash-attention-npu` for the Cube/Vector partitioning).

```cpp
// Online-softmax update for one score block, on the Vector unit.
// scoreBlock : [rowNum, blockLen]  current S_ij = Q·Kj^T (in UB)
// vBlock     : [blockLen, headDim] current V block        (in UB)
// mRun, lRun : [rowNum] running max / running denominator
// oAcc       : [rowNum, headDim] running output accumulator
void OnlineSoftmaxUpdate(const LocalTensor<float>& scoreBlock,
                         const LocalTensor<float>& vBlock,
                         LocalTensor<float>& mRun,
                         LocalTensor<float>& lRun,
                         LocalTensor<float>& oAcc,
                         int rowNum, int blockLen, int headDim) {
    LocalTensor<float> blockMax = buf.Get<float>();   // [rowNum]
    LocalTensor<float> alpha    = buf.Get<float>();   // [rowNum]
    LocalTensor<float> blockSum = buf.Get<float>();   // [rowNum]
    LocalTensor<float> mPrev    = buf.Get<float>();   // [rowNum]

    Adds(mPrev, mRun, 0.0f, rowNum);                  // save m_{i-1}

    // m_i = max(m_{i-1}, rowmax(scoreBlock))
    ReduceMax(blockMax, scoreBlock, rowNum, blockLen);
    Max(mRun, mRun, blockMax, rowNum);

    // alpha = exp(m_{i-1} - m_i)   (correction factor, <= 1)
    Sub(alpha, mPrev, mRun, rowNum);
    Exp(alpha, alpha, rowNum);

    // P = exp(scoreBlock - m_i)    (broadcast m_i over blockLen)
    Sub(scoreBlock, scoreBlock, mRun, rowNum, blockLen);   // s_ij - m_i
    Exp(scoreBlock, scoreBlock, rowNum * blockLen);

    // l_i = l_{i-1} * alpha + rowsum(P)
    ReduceSum(blockSum, scoreBlock, rowNum, blockLen);
    Mul(lRun, lRun, alpha, rowNum);                   // rescale old denom
    Add(lRun, lRun, blockSum, rowNum);

    // O_i = O_{i-1} * alpha + P @ V   (Mul rescales old accumulator)
    Mul(oAcc, oAcc, alpha, rowNum, headDim);          // broadcast alpha
    Matmul(scoreBlock, vBlock, oAcc, rowNum, headDim, blockLen);  // P@V, accumulate
}

// Epilogue, once all blocks are consumed:
//   Div(oAcc, oAcc, lRun)  -> normalized attention output
```

The `Mul` on `oAcc` is the load-bearing rescale: it brings the entire running output onto the new max scale before the current block's `P@V` contribution is added. Note that `Sub`/`Exp` overwrite `scoreBlock` in place to reuse Unified Buffer space, since the raw scores are not needed after exponentiation.

## API Mapping

| Algorithm step | AscendC API | Notes |
|---|---|---|
| `max_j s_ij` (row max) | `ReduceMax` | reduces along the block (key) dimension |
| `m_i = max(m_{i-1}, ·)` | `Max` | elementwise running-max update |
| `α = exp(m_{i-1} − m_i)` | `Sub` + `Exp` | correction factor, in `(0, 1]` |
| `exp(s_ij − m_i)` | `Sub` + `Exp` | stabilized probabilities `P` |
| `Σ_j P` (row sum) | `ReduceSum` | new block's denominator contribution |
| rescale `l`, `O` by `α` | `Mul` | scales running denom and output accumulator |
| `O += P @ V` | `Matmul` | Cube-unit GEMM, accumulates into `oAcc` |
| final normalize | `Div` | `O_N / l_N`, epilogue only |

## Trade-offs, Pitfalls, and Notes

- **Rescale every block, even when the max does not change.** When `m_i == m_{i-1}`, `α = 1` and the `Mul` is a no-op numerically but still issued. Branching to skip it is rarely worth the divergence; keep the update branch-free for predictable Vector-unit scheduling.
- **Keep `m`, `l` in fp32.** Even with fp16 scores and values, the running max and denominator should accumulate in fp32. The denominator `l` can grow over many blocks, and the rescale chain compounds rounding; fp32 statistics preserve the stability that the running-max subtraction provides.
- **Broadcasting axes matter.** `Sub(scoreBlock, scoreBlock, mRun, ...)` and `Mul(oAcc, oAcc, alpha, ...)` broadcast a per-row scalar across the block / head-dim axis. Getting the broadcast stride wrong silently corrupts a subset of rows — validate against `kernel-softmax-ascendc` reference output.
- **Order of operations is fixed.** Update `m` first, derive `α` from the *old* `m`, then rescale `l` and `O`, then add the new block. Rescaling before updating `m`, or exponentiating before the new max is known, breaks the invariant `s_ij − m_i ≤ 0` and reintroduces overflow.
- **Output normalization is deferred.** `O` stays unnormalized (`O_i`, not `O_i / l_i`) until the epilogue. Dividing every block would multiply rounding error and waste Vector cycles; a single final `Div` is both faster and more accurate.
- **Pairs with Cube/Vector overlap.** Because the score `Q·Kᵀ` and the `P@V` accumulation run on the Cube unit while the max/exp/sum reductions run on the Vector unit, online softmax is a natural fit for instruction-queue overlap — the Vector update of block `i` can proceed while the Cube unit produces scores for block `i+1`.

## Relationship to Other Pages

- `kernel-flash-attention-npu` — the primary consumer; this update is its inner loop.
- `kernel-paged-attention-npu` — applies the same running statistics across paged KV-cache blocks, where blocks arrive non-contiguously from the page table.
- `kernel-softmax-ascendc` — the one-pass, max-subtracted softmax this technique generalizes to a streaming form.
