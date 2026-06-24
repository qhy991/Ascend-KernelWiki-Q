---
id: technique-quantization-int8
title: "INT8 Quantization — Per-Token Activation and Per-Channel Weight (W8A8)"
type: wiki-technique
architectures: [ascend910b]
tags: [quantization-int8, int8, w8a8, quantization, optimization]
confidence: source-reported
techniques: [quantization-int8, format-conversion]
hardware_features: [cube-unit, vector-unit]
kernel_types: [matmul, gemm]
related: [kernel-quant-matmul-ascendc, wiki-hardware-cube-unit, technique-format-conversion]
sources: [blog-ascend-w8a8-quantization, doc-ascend-quantization-guide, pr-ascend-pytorch-002]
reproducibility: snippet
---

# INT8 Quantization (W8A8) on Ascend

W8A8 quantizes both the weights and the activations of a linear layer to signed INT8, so the heavy `Q·Kᵀ`-style GEMM runs on the Ascend Cube unit in INT8 rather than FP16. On the 910B Cube, the INT8 datapath roughly doubles the FP16 MAC ceiling (`hw-cube-unit`), and the INT8 weights halve memory footprint and bandwidth. The accuracy cost is contained by quantizing along the *right* axis — per-token dynamic for activations, per-channel static for weights — and by SmoothQuant outlier migration, which moves activation dynamic range into the weights where it is cheaper to represent. This page describes the quant math, the SmoothQuant transform, and the `npu_dynamic_quant` → `npu_quant_matmul` flow that `kernel-quant-matmul-ascendc` implements.

## Why W8A8

A standard FP16 linear layer `Y = X · Wᵀ` spends almost all of its time in the GEMM. Two things make INT8 attractive:

- **Compute.** The 910B Cube unit has a dedicated INT8 MAC path with roughly **2× the FP16 throughput ceiling** (`hw-cube-unit`). An INT8 GEMM that keeps the Cube fed therefore approaches twice the FLOP/s of its FP16 equivalent.
- **Memory.** INT8 weights are half the size of FP16. For the bandwidth-bound, small-batch decode regime this halves weight traffic from global memory, which is often the real bottleneck.

The catch is that INT8 has only 256 levels. Mapping a full activation or weight tensor to those levels with one scale loses too much precision; the technique below recovers it by choosing the quantization *granularity* carefully and by reshaping the activation distribution before quantizing.

## Symmetric Quantization Math

W8A8 on Ascend uses **symmetric** quantization: zero maps to zero, and the representable range is `[-127, 127]` (the value `-128` is avoided so the range stays symmetric and dequant scaling is a single multiply). For a tensor `x` with scale `s`:

```
q = clamp(round(x / s), -127, 127)        # quantize  -> INT8
x ≈ q * s                                  # dequantize -> back to float
```

The scale `s` is computed from the dynamic range of the slice being quantized. For symmetric quant the standard choice is `s = max(|x|) / 127` over whatever axis the granularity dictates, so the largest-magnitude element saturates exactly at `±127`.

### Granularity: per-token activations, per-channel weights

The two operands are quantized along different axes, because their distributions differ:

| Operand | Granularity | Scale shape (for `Y = X·Wᵀ`, `X:[M,K]`, `W:[N,K]`) | When computed |
|---|---|---|---|
| Activation `X` | **per-token** (per row `m`) | `a_scale[M]` | dynamically, at runtime |
| Weight `W` | **per-channel** (per output `n`) | `w_scale[N]` | once, statically (offline) |

- **Per-token dynamic activations.** Each row (token) of `X` gets its own scale, recomputed on the fly from that row's `max(|·|)`. Token activations vary a lot row to row — especially with outlier tokens — so a per-tensor activation scale would be dominated by the worst row. Per-token scaling isolates each row's range. Dynamic (runtime) computation means no calibration set is needed for activations.
- **Per-channel static weights.** Each output channel `n` of `W` gets its own scale, computed once at quantization time and frozen. Weights are fixed after training, so static is exact and free at inference time, and per-channel granularity matches the fact that different output neurons have very different weight magnitudes.

This pairing is what makes the dequant epilogue a clean outer product of scales (see below).

## SmoothQuant Outlier Migration

The hard part of W8A8 is activation outliers: a handful of channels carry values 10–100× the rest, inflating the per-token `max(|·|)` and crushing the resolution of every normal channel. SmoothQuant migrates that difficulty from the activations into the weights, which are easier to quantize.

For each input channel `j`, pick a per-channel smoothing factor `s_j` and apply a diagonal rescaling that the GEMM leaves invariant:

```
x_smooth[:, j] = x[:, j] / s_j          # divide activations down  (per input channel)
W_smooth[:, j] = W[:, j] * s_j          # multiply weights up       (per input channel)
```

Because the GEMM contracts over `j`, `(x / s) · (W * s)ᵀ = x · Wᵀ` exactly — the layer's output is unchanged in full precision. But the *quantization* sees a tamer activation tensor (outlier channels divided down) and a slightly harder weight tensor (corresponding channels scaled up). Since weights are quantized per-channel and statically, they absorb the extra range with little loss, while the activations become far more INT8-friendly. The smoothing factor `s_j` is chosen per input channel from a balance of activation and weight magnitudes (a `max|x_j|` / `max|W_j|` power-law trade-off); it is folded into the weights offline, so SmoothQuant adds **zero runtime cost** beyond the normal per-token quant.

## The Ascend Flow: npu_dynamic_quant → npu_quant_matmul

`torch_npu` exposes the W8A8 path as two ops (see `pr-ascend-pytorch-002`):

1. **`npu_dynamic_quant`** — takes the FP16 activation, computes the per-token `max(|·|)` and scale, and returns the INT8 tensor plus the per-token `a_scale[M]`. This runs on the **Vector unit** (reduction + round + clamp).
2. **`npu_quant_matmul`** — runs the INT8 × INT8 GEMM on the **Cube unit**, accumulating in INT32, then applies the dequant epilogue using `a_scale` and the pre-computed per-channel `w_scale`. This is the op `kernel-quant-matmul-ascendc` wraps.

```python
import torch
import torch_npu

# --- offline: weights are quantized once, per output channel (symmetric) ---
# w_int8 : [N, K] int8,  w_scale : [N] fp32  (SmoothQuant factors already folded into W)
#   w_scale[n] = max(|W_smooth[n, :]|) / 127
#   w_int8[n]  = clamp(round(W_smooth[n] / w_scale[n]), -127, 127)

def w8a8_linear(x_fp16, w_int8, w_scale, bias=None):
    # 1) per-token dynamic quant of the activation on the Vector unit.
    #    x_int8 : [M, K] int8 ;  a_scale : [M] fp32 (= rowmax(|x|)/127)
    x_int8, a_scale = torch_npu.npu_dynamic_quant(x_fp16)

    # 2) INT8 x INT8 GEMM on the Cube unit, INT32 accumulate, then dequant.
    #    npu_quant_matmul folds the dequant scales into its epilogue:
    #      y[m, n] = (int32_acc[m, n]) * a_scale[m] * w_scale[n] (+ bias[n])
    y_fp16 = torch_npu.npu_quant_matmul(
        x_int8,                     # [M, K] int8 activation
        w_int8,                     # [N, K] int8 weight (per-channel quantized)
        scale=w_scale,              # [N] fp32 per-channel weight scale
        pertoken_scale=a_scale,     # [M] fp32 per-token activation scale
        bias=bias,                  # optional [N] fp32 bias, added after dequant
        output_dtype=torch.float16,
    )
    return y_fp16
```

The activation is **never** quantized offline — `npu_dynamic_quant` recomputes `a_scale` per call, which is what makes the activation path robust to whatever distribution the current batch happens to have.

## Dequant Epilogue

The GEMM contracts INT8 operands into an INT32 accumulator, then a single fused epilogue brings the result back to FP16. With per-token activation scales and per-channel weight scales, the dequant is an outer product applied elementwise:

```
int32_acc[m, n] = Σ_k  x_int8[m, k] * w_int8[n, k]          # Cube unit, INT32 accumulate
y[m, n]         = int32_acc[m, n] * a_scale[m] * w_scale[n] (+ bias[n])   # dequant epilogue
```

Each output element is scaled by exactly two numbers — its row's activation scale `a_scale[m]` and its column's weight scale `w_scale[n]` — which is why the per-token / per-channel pairing is so convenient: the epilogue needs no cross-terms. The scaling runs on the **Vector unit** as part of the fused op, so the INT32 accumulator never lands in global memory in raw form. The optional `bias` is in FP32 and is added *after* dequant (it lives in the output domain, not the INT8 domain).

## Performance and Accuracy Trade-offs

| Aspect | FP16 baseline | W8A8 (INT8) |
|---|---|---|
| Cube MAC ceiling (910B) | 1× | **~2×** (`hw-cube-unit`) |
| Weight memory / bandwidth | 1× | ~0.5× |
| Activation quant cost | — | per-token reduction on Vector unit, per call |
| Weight quant cost | — | one-time, offline |
| Outlier robustness | n/a | recovered by SmoothQuant |
| Accuracy | reference | small degradation; SmoothQuant + granularity keep it near-FP16 |

The compute and memory wins are concrete; the accuracy outcome is workload-dependent, which is why this page is marked `source-reported` rather than `verified`. The grounding sources report that the per-token + per-channel + SmoothQuant combination keeps degradation small on the reported models, not that it is lossless.

## Trade-offs, Pitfalls, and Notes

- **Match the granularity to the axis the scale multiplies.** Per-token activation scales index the GEMM's `M` axis; per-channel weight scales index the `N` axis. Quantizing weights per-token, or activations per-channel, breaks the clean `a_scale[m] * w_scale[n]` epilogue and forces a far more expensive dequant — keep activations per-row and weights per-output-channel.
- **Keep scales in FP32.** `a_scale`, `w_scale`, and the dequant arithmetic should be FP32 even when inputs and outputs are FP16. The INT32 accumulator spans a wide range and the two-scale product can be small; FP16 scales lose precision exactly where it matters.
- **Avoid `-128`.** Symmetric W8A8 clamps to `[-127, 127]`, not the full INT8 `[-128, 127]`. Using `-128` would make the negative range asymmetric and invalidate the single-multiply dequant. The `round` is round-half-to-even before the clamp.
- **SmoothQuant must be folded once, consistently.** The smoothing factors `s_j` divide activations and multiply weights along the *same* input-channel axis `j`. If the factors used to fold the weights differ from the ones implied by the activation distribution at runtime, the `(x/s)·(W·s)ᵀ = x·Wᵀ` invariance is lost and accuracy collapses. Since `s_j` is baked into `W_smooth` offline, the runtime path applies *no* per-channel activation scaling — only per-token.
- **Activation quant is recurring overhead.** Unlike static weight quant, `npu_dynamic_quant` runs on every forward pass. It is cheap (a per-row reduce + round + clamp on the Vector unit) and overlaps with the Cube GEMM, but for very small `K` it can erode the INT8 compute win — favor W8A8 where the GEMM dominates.
- **Layout still matters.** The Cube unit wants its INT8 operands in the fractal layout; the ND→NZ packing described in `technique-format-conversion` applies to the INT8 tensors just as it does to FP16, and a fused CopyIn keeps the conversion off the critical path.

## Relationship to Other Pages

- `kernel-quant-matmul-ascendc` — the INT8 GEMM kernel that consumes `x_int8`, `w_int8`, `a_scale`, and `w_scale` and applies this dequant epilogue.
- `hw-cube-unit` — the source of the ~2× INT8-over-FP16 compute ceiling on the 910B.
- `technique-format-conversion` — the ND↔NZ packing the INT8 operands need before reaching the Cube unit.
