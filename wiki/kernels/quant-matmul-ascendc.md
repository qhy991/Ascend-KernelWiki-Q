---
id: kernel-quant-matmul-ascendc
title: "AscendC W8A8 INT8 Matmul — npu_quant_matmul"
type: wiki-kernel
architectures: [ascend910b]
tags: [quant-matmul, matmul, int8, quantization, ascendc]
confidence: source-reported
kernel_types: [matmul, gemm]
languages: [ascendc, python]
sources: [blog-ascend-w8a8-quantization, pr-ascend-pytorch-002, doc-ascend-quantization-guide]
related: [kernel-matmul-ascendc, technique-quantization-int8, wiki-hardware-cube-unit]
techniques: [quantization-int8, format-conversion, nz-tiling]
performance_claims:
  - gpu: Ascend 910B
    dtype: int8
    shape: "M=4096, N=4096, K=4096"
    metric: speedup
    value: 2.0
    utilization: "INT8 Cube throughput vs fp16 baseline"
    source_id: blog-ascend-w8a8-quantization
reproducibility: snippet
operator_recipe:
  operator: quant-matmul
  dtype: [int8, fp16, bf16]
  layout: [ND-activation, NZ-weight, dequantized-output]
  shape_class: [large-gemm, decode-gemm, quantized-transformer]
  memory_path:
    global_memory: [int8-activation, int8-weight, pertoken-scale, weight-scale, output]
    onchip_buffers: [UB, L1, L0A, L0B, L0C]
    data_formats: [ND-activation, FRACTAL_NZ-weight]
  parallelism:
    granularity: output tiles over M and N with K reduction
    block_dim: AI Cube core count
    sync_scope: per-tile dequant epilogue
  instruction_family: [INT8-Mmad, Vector-dequant]
  library_backend: [torch_npu, aclnn, AscendC]
  tiling:
    tile_axes: [M, N, K]
    tile_granularity: Cube INT8 tiles plus Vector dequant rows/columns
    constraints: [NZ-weight-layout, per-token-scale-by-M, per-channel-scale-by-N]
  pipeline:
    stages: [DynamicQuant, INT8Mmad, DequantEpilogue, CopyOut]
    queues: [MTE, Cube, Vector]
    overlap: Vector scale/dequant work overlaps the next Cube tile when tiling is large enough
  aicore_mapping:
    block_dim: aicCoreNum
    scheduling: quantized GEMM output tiles distributed across AI Cube cores
  data_movement:
    apis: [DataCopy, LoadData]
    path: "GM int8/scales -> UB/L1/L0 -> INT32 accumulator -> Vector dequant -> GM"
  compute_path:
    units: [Cube Unit, Vector Unit]
    primitives: [Mmad, Cast, Mul, Add]
---

# AscendC W8A8 INT8 Matmul

W8A8 quantizes both weights and activations to INT8, letting the Ascend 910B Cube unit run INT8×INT8 multiply-accumulate at roughly twice the FP16 throughput while accumulating in INT32. The quantized GEMM is exposed in `torch_npu` as `npu_quant_matmul` (QMM); activations are quantized per-token at runtime via `npu_dynamic_quant`, weights are pre-quantized per-channel and stored INT8 in NZ format, and a fused dequant epilogue restores fp16/bf16 output. The headline 2× is a hardware compute ceiling (910B INT8 ~640 TOPS vs FP16 ~320 TOPS), not a measured end-to-end speedup.

## Quantization Pipeline

The W8A8 path replaces a single FP16 matmul with a four-stage pipeline:

1. **Per-token dynamic quant** — activations `x (fp16/bf16, M×K)` are quantized row-wise by `npu_dynamic_quant`, producing `x_int8 (M×K)` and `pertoken_scale (M,)`. Each token (row) gets its own scale, which preserves accuracy across rows with very different magnitudes.
2. **INT8 Cube matmul** — `x_int8 @ x2_int8` runs on the Cube unit with INT32 accumulation, yielding `acc (INT32, M×N)`. Weights `x2_int8 (K×N)` are pre-quantized per-channel (per output column) offline.
3. **Dequant epilogue** — the INT32 accumulator is scaled back to float: `out[m,n] = acc[m,n] * pertoken_scale[m] * weight_scale[n]`. The per-row `pertoken_scale` and per-column `weight_scale` factor out cleanly because both quantizations are symmetric and per-channel.
4. **Optional bias + cast** — an fp32/int32 `bias` is added, then the result is cast to the requested `output_dtype` (fp16 or bf16).

Stages 2–4 are fused inside the `npu_quant_matmul` kernel, so the INT32 accumulator never round-trips to global memory.

## Python (torch_npu) Usage

```python
import torch
import torch_npu

# Activations: per-token dynamic quant (runtime)
#   x: [M, K] fp16/bf16 on NPU
x_int8, pertoken_scale = torch_npu.npu_dynamic_quant(x)
#   x_int8:        [M, K] int8
#   pertoken_scale:[M]    fp32  (one scale per token / row)

# Weights: pre-quantized per-channel, stored INT8 in NZ layout
#   x2_int8:      [K, N] int8   (per-column / per-channel quantized offline)
#   weight_scale: [N]    fp32   (one scale per output channel)
bias = None  # optional, [N] int32 / fp32

out = torch_npu.npu_quant_matmul(
    x_int8,                 # x1: int8 activations  [M, K]
    x2_int8,                # x2: int8 weights      [K, N]
    scale=weight_scale,     # per-channel (per-column) weight scale [N]
    pertoken_scale=pertoken_scale,  # per-token (per-row) act scale [M]
    bias=bias,              # optional bias         [N]
    output_dtype=torch.float16,     # dequantized output dtype
)
# out: [M, N] fp16  ==  (x_int8 @ x2_int8).int32  *  pertoken_scale[:,None] * weight_scale[None,:]  (+ bias)
```

`npu_quant_matmul` requires `x2_int8` in NZ format for peak Cube utilization; weights are converted once at load time and cached, so format conversion is off the hot path (see [technique-quantization-int8](technique-quantization-int8) and the NZ tiling used by [kernel-matmul-ascendc](kernel-matmul-ascendc)).

## AscendC Dequant Epilogue Sketch

The compute body is the same Cube tiling as the FP16 GEMM in [kernel-matmul-ascendc](kernel-matmul-ascendc), but the MAD result lives in an INT32 accumulator. The epilogue runs on the Vector unit, overlapped with the next Cube tile:

```cpp
// Per output tile [TILE_M, TILE_N], after Cube INT8 MAD -> acc_i32 in UB
// pertoken_scale[m] : per-row  (M,)  fp32
// weight_scale[n]   : per-col  (N,)  fp32
void QuantMatmulEpilogue(
        LocalTensor<int32_t>& acc_i32,      // [TILE_M, TILE_N] INT32 accumulator
        LocalTensor<float>&   pertoken,     // [TILE_M] per-token scales (broadcast over N)
        LocalTensor<float>&   wscale,       // [TILE_N] per-channel scales (broadcast over M)
        LocalTensor<float>&   bias,         // [TILE_N] optional bias, or empty
        LocalTensor<half>&    out_fp16) {   // [TILE_M, TILE_N] fp16 output

    LocalTensor<float> acc_f32 = AllocUB<float>(TILE_M * TILE_N);

    // 1. INT32 accumulator -> FP32
    Cast(acc_f32, acc_i32, RoundMode::CAST_NONE, TILE_M * TILE_N);

    // 2. Dequant: acc * pertoken_scale[m] (per row) * weight_scale[n] (per col)
    for (int m = 0; m < TILE_M; ++m) {
        // row slice [TILE_N]
        LocalTensor<float> row = acc_f32[m * TILE_N];
        Muls(row, row, pertoken.GetValue(m), TILE_N);   // * per-token scale
        Mul(row, row, wscale, TILE_N);                  // * per-channel scale
        if (bias.GetSize() > 0) {
            Add(row, row, bias, TILE_N);                // + optional bias
        }
    }

    // 3. Cast back to requested output dtype (fp16 here)
    Cast(out_fp16, acc_f32, RoundMode::CAST_RINT, TILE_M * TILE_N);
}
```

The two scale multiplies are cheap Vector ops and hide under Cube MAD latency, so the epilogue adds little to the critical path on a well-tiled kernel.

## The ~2× Compute Ceiling

The 910B Cube unit issues INT8 MACs at roughly double the FP16 rate, giving the theoretical headroom below:

| Path        | Cube dtype | Accumulate | 910B peak (approx) | Relative |
|-------------|------------|------------|--------------------|----------|
| FP16 matmul | fp16       | fp32       | ~320 TOPS          | 1.0×     |
| W8A8 QMM    | int8       | int32      | ~640 TOPS          | 2.0×     |

This 2× is a **hardware ceiling**, not an end-to-end number. Realized speedup is lower because of the dynamic-quant prologue, the dequant epilogue, and the fact that many transformer matmuls are memory- or latency-bound rather than Cube-bound. Treat `value: 2.0` in the frontmatter as the theoretical Cube doubling, consistent with the `source-reported` confidence — no measured throughput is claimed here.

## Accuracy: SmoothQuant Dependency

Naive per-tensor INT8 activation quantization collapses accuracy on LLMs because activation channels contain large outliers. The W8A8 recipe here relies on two mitigations:

- **Per-token dynamic quant** of activations (each row scaled independently), so a high-magnitude token does not crush the resolution of others.
- **SmoothQuant**-style pre-processing offline, which migrates activation outlier magnitude into the weights via a per-channel smoothing factor before weights are quantized per-channel. Without this rebalancing, even per-token quant leaves channel outliers that degrade INT8 GEMM accuracy.

Per-channel weight scales (`scale`) and per-token activation scales (`pertoken_scale`) are what make the factored dequant `acc * pertoken_scale[m] * weight_scale[n]` both correct and accurate.

## Trade-offs and Pitfalls

- **Ceiling vs. realized**: the 2× is Cube-bound peak. For small-M decode matmuls (memory-bound), expect well under 2×.
- **Prologue cost**: `npu_dynamic_quant` adds a per-token reduction over K each step; it is fused-friendly but not free.
- **NZ weights**: `x2_int8` must be in NZ for peak Cube utilization. Quantize and convert weights once at load, never per-step.
- **Scale dtype/shape**: `pertoken_scale` is length-M (per row), `scale` is length-N (per column). Swapping them silently produces wrong results.
- **Accuracy is recipe-dependent**: dropping SmoothQuant or falling back to per-tensor activation quant can break LLM accuracy even though the kernel still runs.
- **Symmetric quant assumed**: the clean factored dequant assumes symmetric (zero-point-free) per-channel/per-token quantization; asymmetric schemes need an extra correction term.

## Related Pages

- [kernel-matmul-ascendc](kernel-matmul-ascendc) — FP16 Cube GEMM, the tiling and NZ foundation this kernel reuses.
- [technique-quantization-int8](technique-quantization-int8) — per-token/per-channel INT8 quantization and SmoothQuant background.
- [wiki-hardware-cube-unit](hw-cube-unit) — INT8 vs FP16 MAC throughput on the 910B Cube unit.
