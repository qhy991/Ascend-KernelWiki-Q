---
id: kernel-rmsnorm-ascendc
title: "AscendC RMSNorm — Fused Vector Normalization"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [rmsnorm, layernorm, vector-unit, ascendc]
confidence: source-reported
kernel_types: [rmsnorm, layernorm]
languages: [ascendc]
sources: [doc-ascendc-api-reference, blog-ascendc-performance-tips, doc-ascend-operator-fusion]
related: [kernel-layernorm-ascendc, wiki-hardware-vector-unit, technique-online-softmax]
techniques: [data-reuse, pipeline-scheduling]
reproducibility: snippet
operator_recipe:
  operator: rmsnorm
  dtype: [fp16, bf16, fp32]
  layout: [row-major, token-by-hidden-dim]
  shape_class: [normalization, memory-bound, transformer-row]
  memory_path:
    global_memory: [x, gamma, y]
    onchip_buffers: [UB]
    data_formats: [contiguous-row]
  parallelism:
    granularity: one or more token rows per AICore
    block_dim: row tiles across Vector-capable AICores
    sync_scope: per-row reduction only
  instruction_family: [Vector-reduce, Vector-elementwise]
  library_backend: [AscendC]
  tiling:
    tile_axes: [row, hidden-dim]
    tile_granularity: hidden-dim row tile sized to UB
    constraints: [UB-capacity, reduction-buffer-size, gamma-reuse]
  pipeline:
    stages: [CopyIn, SquareAndReduce, RsqrtAndScale, CopyOut]
    queues: [MTE, Vector]
    overlap: next row DataCopy overlaps current row vector reduction and scale
  aicore_mapping:
    block_dim: row-tile count
    scheduling: distribute independent token rows across Vector-capable AICores
  data_movement:
    apis: [DataCopy]
    path: "GM row/gamma -> UB -> Vector reduce/scale -> GM output"
  compute_path:
    units: [Vector Unit]
    primitives: [Mul, ReduceSum, Rsqrt, Muls]
---

# AscendC RMSNorm — Fused Vector Normalization

Root Mean Square Layer Normalization (RMSNorm) normalizes each token row by its root-mean-square magnitude and rescales by a learned `gamma`, omitting the mean-centering and `beta` shift of classic LayerNorm. On Ascend NPU it maps cleanly onto the Vector unit as a single fused pipeline: one reduction over each row, a scalar reciprocal-square-root, and two broadcast multiplies. Because it needs only one reduction and no mean subtraction, RMSNorm is strictly cheaper than the LayerNorm kernel described in `kernel-layernorm-ascendc`.

## Mathematical Formulation

```
ms   = sum(x^2) / n          # mean of squares over the hidden dimension
rms  = sqrt(ms + eps)
y    = (x / rms) * gamma
```

There is no `mean = sum(x)/n` pass and no `beta` add. The only per-row reduction is the sum of squares, and the only per-row scalar is `1 / rms`, which is applied as a broadcast factor across the row before the per-element `gamma` scale.

## Why RMSNorm Is Cheaper than LayerNorm

The contrast with `kernel-layernorm-ascendc` is the core motivation for using RMSNorm in transformer blocks:

| Aspect                  | LayerNorm                          | RMSNorm                       |
|-------------------------|------------------------------------|-------------------------------|
| Reductions per row      | 2 (sum for mean, sum for variance) | 1 (sum of squares)            |
| Mean centering          | Yes (`Sub` of mean broadcast)      | No                            |
| Learned parameters      | `gamma` + `beta`                   | `gamma` only                  |
| Vector ops on hot path  | Sub, Mul, ReduceSum, Sqrt, Div, Mul, Add | Mul, ReduceSum, Rsqrt, Mul, Mul |
| Extra GM read           | `beta`                             | none                          |

Dropping the mean pass removes one full reduction and one broadcast `Sub` over the hidden dimension, which is why RMSNorm is the normalization of choice in LLaMA-family models where it is invoked twice per transformer layer.

## Vector-Unit Pipeline

The kernel follows the standard AscendC three-stage structure — **CopyIn → Compute → CopyOut** — with each stage driven by a `TQue`. One row (length `hidden_dim`) is the tiling granularity.

### Stage 1 — CopyIn (VECIN)

`DataCopy` brings a row of `x` from Global Memory into a `LocalTensor` held in a `TQue<TPosition::VECIN>`. `gamma` is resident for the whole hidden dimension and is loaded once.

### Stage 2 — Compute

1. **Square**: `Mul(sq, x, x, hidden_dim)` produces `x^2` elementwise.
2. **Reduce**: `ReduceSum(ss, sq, hidden_dim)` collapses the row to the scalar sum of squares.
3. **Scalar rsqrt**: divide by `n`, add `eps`, and take `Rsqrt` to obtain `1 / rms` as a scalar.
4. **Broadcast scale**: `Mul(x, x, rrms, hidden_dim)` multiplies every element by the scalar `1 / rms`.
5. **Gamma scale**: `Mul(y, x, gamma, hidden_dim)` applies the per-channel weight.

### Stage 3 — CopyOut (VECOUT)

`DataCopy` writes the normalized row from a `TQue<TPosition::VECOUT>` `LocalTensor` back to Global Memory.

The `TQue` double-buffering lets the MTE (DataCopy) of the next row overlap the Vector compute of the current row, so for large `hidden_dim` the kernel approaches memory-bandwidth bound — the desired regime for a normalization op.

## AscendC Code Example

```cpp
class KernelRmsNorm {
public:
    __aicore__ inline void Init(__gm__ uint8_t* x, __gm__ uint8_t* gamma,
                                __gm__ uint8_t* y, uint32_t rows,
                                uint32_t hiddenDim, float eps) {
        this->hiddenDim = hiddenDim;
        this->rows      = rows;
        this->eps       = eps;
        this->avgFactor = 1.0f / static_cast<float>(hiddenDim);

        xGm.SetGlobalBuffer((__gm__ float*)x, rows * hiddenDim);
        yGm.SetGlobalBuffer((__gm__ float*)y, rows * hiddenDim);
        gammaGm.SetGlobalBuffer((__gm__ float*)gamma, hiddenDim);

        // Allocate queues on the Unified Buffer
        pipe.InitBuffer(inQueueX, BUFFER_NUM, hiddenDim * sizeof(float));
        pipe.InitBuffer(inQueueG, 1,          hiddenDim * sizeof(float));
        pipe.InitBuffer(outQueueY, BUFFER_NUM, hiddenDim * sizeof(float));
        pipe.InitBuffer(tmpBuf,   hiddenDim * sizeof(float));   // x^2 scratch
        pipe.InitBuffer(reduceBuf, sizeof(float));              // sum-of-squares
    }

    __aicore__ inline void Process() {
        // gamma is reused across every row -> load once
        LocalTensor<float> gammaLocal = inQueueG.AllocTensor<float>();
        DataCopy(gammaLocal, gammaGm, hiddenDim);
        inQueueG.EnQue(gammaLocal);
        gammaLocal = inQueueG.DeQue<float>();

        for (uint32_t r = 0; r < rows; ++r) {
            CopyIn(r);
            Compute(gammaLocal);
            CopyOut(r);
        }
        inQueueG.FreeTensor(gammaLocal);
    }

private:
    __aicore__ inline void CopyIn(uint32_t r) {
        LocalTensor<float> xLocal = inQueueX.AllocTensor<float>();
        DataCopy(xLocal, xGm[r * hiddenDim], hiddenDim);
        inQueueX.EnQue(xLocal);
    }

    __aicore__ inline void Compute(LocalTensor<float>& gammaLocal) {
        LocalTensor<float> xLocal  = inQueueX.DeQue<float>();
        LocalTensor<float> yLocal  = outQueueY.AllocTensor<float>();
        LocalTensor<float> sq      = tmpBuf.Get<float>();
        LocalTensor<float> ss      = reduceBuf.Get<float>();

        // 1. square  -> 2. sum of squares (single reduction)
        Mul(sq, xLocal, xLocal, hiddenDim);
        ReduceSum(ss, sq, sq, hiddenDim);

        // 3. scalar rsqrt of mean-of-squares + eps
        float sumSq = ss.GetValue(0);
        float rrms  = 1.0f / sqrt(sumSq * avgFactor + eps);   // == Rsqrt(ms + eps)

        // 4. broadcast scale by 1/rms, then 5. per-channel gamma
        Muls(xLocal, xLocal, rrms, hiddenDim);                // x * (1/rms)
        Mul(yLocal, xLocal, gammaLocal, hiddenDim);           // * gamma

        outQueueY.EnQue(yLocal);
        inQueueX.FreeTensor(xLocal);
    }

    __aicore__ inline void CopyOut(uint32_t r) {
        LocalTensor<float> yLocal = outQueueY.DeQue<float>();
        DataCopy(yGm[r * hiddenDim], yLocal, hiddenDim);
        outQueueY.FreeTensor(yLocal);
    }

    TPipe pipe;
    TQue<TPosition::VECIN,  BUFFER_NUM> inQueueX;
    TQue<TPosition::VECIN,  1>          inQueueG;
    TQue<TPosition::VECOUT, BUFFER_NUM> outQueueY;
    TBuf<TPosition::VECCALC> tmpBuf, reduceBuf;

    GlobalTensor<float> xGm, yGm, gammaGm;
    uint32_t hiddenDim, rows;
    float eps, avgFactor;
    static constexpr int32_t BUFFER_NUM = 2;
};
```

The scalar `1/rms` can alternatively be produced with the Vector `Rsqrt` intrinsic on a length-1 tensor (`Adds` to add `eps`, then `Rsqrt`); the scalar form above keeps the rescale entirely on the scalar unit so it overlaps the next row's reduction. `Muls` (scalar-broadcast multiply) is used for the `1/rms` factor, while the per-channel `gamma` uses the two-tensor `Mul`.

## Fusion Opportunities

RMSNorm rarely runs alone. The dominant fusion — captured by the `torch_npu` operator `npu_rms_norm(x, gamma, eps)` and its residual-add variant — folds the transformer residual into the same kernel:

```
# Pre-norm transformer block, fused on the Vector unit
hidden = hidden + sublayer_out          # residual Add, kept in UB
normed = npu_rms_norm(hidden, gamma, eps)
```

By keeping the residual sum in the Unified Buffer (an extra `Add` before the square step), the fused kernel avoids a round-trip of `hidden` to Global Memory between the residual and the normalization. This is the same data-reuse principle described in `technique-data-reuse`, and it is why operator-fusion passes (see `doc-ascend-operator-fusion`) target the add+RMSNorm pair specifically. The `npu_rms_norm` PyTorch op is the standard reference for numerical parity when validating a hand-written AscendC kernel.

## Trade-offs, Pitfalls, and Notes

- **Single reduction, but still bandwidth-bound.** Like LayerNorm, RMSNorm reads `x` and writes `y` once. Removing the second reduction cuts Vector compute, not memory traffic, so on Ascend 910B the kernel is bound by Unified Buffer / Global Memory bandwidth for large hidden dimensions; the win over LayerNorm shows up most when the Vector pipeline was the bottleneck (small batches, fp32).
- **Reduction precision.** Summing `x^2` in fp16 loses precision for long hidden dimensions. Accumulate the sum of squares in fp32 even when `x` is fp16, then cast back after the `gamma` multiply. The grounding APIs (`Mul`, `ReduceSum`, `Rsqrt`) support mixed-precision accumulation buffers.
- **`eps` placement.** `eps` is added inside the square root (`sqrt(ms + eps)`), not outside. Adding it to the reciprocal instead changes the result and breaks parity with `npu_rms_norm`.
- **Broadcast vs. per-channel.** The `1/rms` factor is a per-row scalar (use `Muls` / a scalar broadcast), whereas `gamma` is per-channel (use elementwise `Mul`). Swapping these is a common transcription bug.
- **No `beta`.** RMSNorm has no bias term; do not add a `beta` `Add` stage by analogy with `kernel-layernorm-ascendc`.
- **Tiling.** When `hidden_dim` exceeds the per-queue Unified Buffer slice, split the row into column tiles and accumulate the partial sums of squares across tiles before the `Rsqrt`; this mirrors the streaming-reduction pattern used in `technique-online-softmax`.

## Summary

RMSNorm on Ascend NPU is a textbook Vector-unit kernel: `Mul` to square, `ReduceSum` for the single per-row reduction, a scalar `Rsqrt` of `mean-of-squares + eps`, and two multiplies (`Muls` for `1/rms`, `Mul` for `gamma`), all wrapped in a `TPipe` + `TQue<VECIN/VECOUT>` CopyIn/Compute/CopyOut pipeline. It is consistently lighter than the LayerNorm kernel in `kernel-layernorm-ascendc` thanks to the missing mean pass, and it fuses naturally with the residual add through the `npu_rms_norm` operator path.
