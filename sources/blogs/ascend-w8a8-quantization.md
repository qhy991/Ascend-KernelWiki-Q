---
id: blog-ascend-w8a8-quantization
title: "W8A8 INT8 Quantization on Ascend 910B — SmoothQuant and npu_quant_matmul"
type: source-blog
author: modelarts-team
date: '2026-04-22'
url: https://support.huaweicloud.com/intl/en-us/bestpractice-modelarts/modelarts_llm_infer_5906011.html
architectures: [ascend910b]
tags: [quantization, int8, w8a8, python, ascendc]
techniques: [format-conversion]
hardware_features: [cube-unit, vector-unit]
kernel_types: [matmul, gemm]
languages: [python, ascendc]
confidence: source-reported
---

# W8A8 INT8 Quantization on Ascend 910B

W8A8 quantizes both LLM weights and activations to INT8, letting the linear layers run on the 910B Cube unit in INT8 instead of FP16. This best-practice guide from the ModelArts team covers the quantization recipe (SmoothQuant + per-token/per-channel scales) and the inference-time `npu_quant_matmul` (QMM) operator that fuses INT8 matmul with on-the-fly dequantization. On 910B the INT8 Cube pipeline delivers roughly 2× the throughput of FP16, which is the main reason W8A8 is attractive for decode-bound serving.

## What W8A8 Means

"W8A8" is shorthand for **INT8 weights, INT8 activations**. Both operands of the linear-layer matmul are quantized to 8-bit integers, so the Cube unit performs INT8×INT8 multiply-accumulate with an INT32 accumulator, then a dequant step scales the INT32 result back to FP16/BF16.

The two operands are quantized differently:

| Tensor | Granularity | Symmetric? | Scale computed | Scale shape (for `Y = X·Wᵀ`) |
|--------|-------------|------------|----------------|-------------------------------|
| Activation `X` | per-token (per-row) | symmetric | dynamically at runtime | `[M, 1]` |
| Weight `W` | per-channel | symmetric | statically, offline | `[1, N]` |

- **Per-token (dynamic) activation quant**: each row of the activation matrix (one token's hidden vector) gets its own scale, recomputed at inference time from the live tensor. This adapts to the wide dynamic range that varies token-to-token in transformer activations.
- **Per-channel (static) weight quant**: each output channel of the weight matrix gets a fixed scale, computed once when the model is quantized. Weights are constant, so their scales can be baked in.

Both quant schemes are **symmetric** (zero-point fixed at 0), so the dequant is a pure scale multiply with no offset subtraction on the integer values.

## The Outlier Problem and SmoothQuant

Activation tensors in LLMs contain a small number of channels with very large magnitudes ("outlier" channels). Per-token quantization alone still has to cover those outliers within a single row's scale, which crushes the precision of the well-behaved channels and degrades accuracy badly under INT8.

**SmoothQuant** addresses this by migrating the difficulty from activations into weights *before* quantization. For each channel `j` it picks a smoothing factor `s_j` and rescales:

```
X̂ = X / s        (activation divided by s, outliers shrink)
Ŵ = W · s        (weight multiplied by s, absorbs the magnitude)
```

Because `X̂ · Ŵᵀ = X · Wᵀ`, the math is mathematically equivalent — the product is unchanged. The factor `s` is chosen to **balance** the quantization difficulty between the two operands, typically from the per-channel activation and weight magnitudes (an `alpha` migration-strength hyperparameter trades off how much outlier magnitude is pushed into the weights). After smoothing, both `X̂` and `Ŵ` quantize cleanly to INT8.

SmoothQuant is applied offline during model preparation. The smoothing factors are folded into the preceding LayerNorm/weight tensors, so there is **no extra runtime op** for smoothing — the inference graph just sees already-smoothed INT8 weights.

## Inference-Time Operator: npu_quant_matmul (QMM)

At inference the quantized linear layer runs through `torch_npu.npu_quant_matmul`. It takes the INT8 activation and INT8 weight, performs the matmul on the Cube unit with INT32 accumulation, and applies the per-token × per-channel dequant in one fused operator. The signature follows:

```python
import torch
import torch_npu

# w_int8:        [K, N] INT8 weight, pre-converted to NZ format (see below)
# weight_scale:  [N]    per-channel (per-column) weight scale, static
# x_int8:        [M, K] INT8 activation, per-token quantized at runtime
# pertoken_scale:[M]    per-token (per-row) activation scale
# offset:        None for symmetric quant
# bias:          optional INT32/FP32 bias added after accumulation
# output_dtype:  torch.float16 (or bfloat16) for the dequantized result

# 1) dynamic per-token activation quant just before the matmul
x_int8, pertoken_scale = torch_npu.npu_dynamic_quant(x)

# 2) INT8xINT8 matmul + fused dequant. Weight (per-channel) and activation
#    (per-token) scales are passed on SEPARATE arguments, not pre-combined.
y = torch_npu.npu_quant_matmul(
    x_int8,                          # x1: INT8 activations [M, K]
    w_int8,                          # x2: INT8 weights     [K, N] (NZ)
    scale=weight_scale,              # per-channel weight scale [N]
    offset=None,                     # symmetric quant -> no zero-point
    pertoken_scale=pertoken_scale,   # per-token activation scale [M]
    bias=bias,
    output_dtype=torch.float16,
)
```

The data path inside the operator:

1. **INT8 × INT8 matmul** on the Cube unit — INT32 accumulator holds the raw integer dot products.
2. **Dequant** — the INT32 accumulator is rescaled by the per-token activation scale (`pertoken_scale`, `[M]`, broadcast over columns) and the per-channel weight scale (`scale`, `[N]`, broadcast over rows): `out[m,n] = acc[m,n] * pertoken_scale[m] * scale[n]`; the elementwise dequant runs on the Vector unit.
3. **Bias add** and **cast to `output_dtype`** (FP16/BF16) complete the epilogue.

Because the activation scale is dynamic, `npu_dynamic_quant` produces the per-token scale just before QMM and it is passed on the dedicated `pertoken_scale` argument; the per-channel weight `scale` is a static tensor stored with the model.

### Activation quantization before QMM

The dynamic per-token activation quant computes, per row, `scale_row = max(|x_row|) / 127` and `x_int8 = round(x / scale_row)`, clamped to `[-127, 127]`. This row scale is what gets combined with the static weight scale to form QMM's `scale` argument.

## Weights in NZ Format

For the Cube unit to reach peak INT8 throughput, the INT8 weight tensor is **pre-converted to NZ (fractal) format** offline, so no layout conversion happens on the hot path. This mirrors the FP16 GEMM guidance — see `blog-nz-format-explained` for why NZ matches the Cube unit's L0 fractal tiling, and `kernel-matmul-ascendc` for the general matmul tiling that the quantized path inherits. The only ND↔NZ conversion left at runtime is, at most, on the activation side at layer boundaries (the `format-conversion` technique).

## Why It's Faster: INT8 vs FP16 on 910B

The payoff comes from the Cube unit's INT8 rate. On Ascend 910B the INT8 Cube throughput is roughly **2× the FP16 rate** (theoretical):

| Precision | 910B Cube peak (theoretical) | Relative |
|-----------|------------------------------|----------|
| FP16 | ~320 TFLOPS | 1× |
| INT8 (W8A8) | ~640 TOPS | ~2× |

In practice the speedup of an end-to-end linear layer is less than 2× because of the activation-quant and dequant epilogue overhead, but the matmul itself — the dominant cost in LLM decode — runs at the INT8 rate. W8A8 also roughly halves weight memory footprint and weight-load bandwidth versus FP16, which helps the memory-bound decode phase further.

## Trade-offs, Pitfalls, and Notes

- **Accuracy depends on SmoothQuant calibration.** Without smoothing, naive INT8 activation quant on LLMs can lose several points of accuracy. The `alpha` migration strength must be tuned per model family; too aggressive over-loads the weights with outliers and vice versa.
- **Dynamic per-token quant is not free.** Computing per-row max and quantizing the activation adds a Vector-unit pass before every QMM. For very small `M` (single-token decode) this overhead is proportionally larger, so the realized speedup is below the theoretical 2×.
- **Symmetric only here.** This recipe uses symmetric quant for both operands, so `offset=None`. Asymmetric schemes would need a zero-point and a more expensive dequant — not used in this W8A8 path.
- **Per-channel weight + per-token activation is mandatory.** Per-tensor (single scalar) scales were tried in early INT8 work and do not hold accuracy for LLMs; the per-channel/per-token combination is what makes W8A8 usable.
- **Not all layers are quantized.** Sensitive layers (e.g. the LM head, sometimes specific attention projections) are often kept in FP16. W8A8 is typically applied to the bulk MLP and projection linear layers.
- **NZ conversion is offline.** Convert weights to NZ once at model load; doing it per-step would erase the throughput win — keep weights resident in NZ.
- **Confidence**: figures here are the vendor-reported theoretical Cube rates (~640 TOPS INT8 vs ~320 TFLOPS FP16). Real serving throughput depends on batch size, sequence length, and how much of the model is quantized — measure with `msprof` before claiming a speedup.

## Related Resources

- [NZ Format Explained](blog-nz-format-explained) — why the Cube unit wants NZ-laid weights
- [AscendC Matmul Kernel](kernel-matmul-ascendc) — the underlying tiled matmul the quantized path builds on
- [Cube Unit Architecture](hw-cube-unit) — INT8/FP16 throughput characteristics on 910B
- [AscendC Performance Tips](blog-ascendc-performance-tips) — keeping data in NZ and overlapping Cube/Vector work
