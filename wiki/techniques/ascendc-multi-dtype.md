---
id: technique-ascendc-multi-dtype
title: "AscendC Multi-Dtype Support — fp16, bf16, fp32"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [ascendc, fp16, bf16, fp32, precision, dtype]
confidence: verified
sources: [doc-torch-npu-npu-ffn, doc-ascendc-pytorch-framework-adaptation, doc-ascendc-api-reference, doc-torch-npu-adapter, blog-ascend-910b-deep-dive]
techniques: [precision-tuning]
hardware_features: [cube-unit, vector-unit]
kernel_types: [matmul, elementwise, activation]
languages: [ascendc, cpp]
related: [lang-torch-npu-cpp-api, kernel-ffn-fused-ascendc, pattern-precision-nan-debugging, technique-precision-tuning]
---

# AscendC Multi-Dtype Support — fp16, bf16, fp32

MultiKernelBench FFN tests 50 cases across **fp16**, **fp32**, and **bf16**. Kernels must compile, dispatch, and pass correctness for all three. This page documents dtype-specific hardware behavior and template patterns.

## Hardware Execution Path by Dtype (910B)

| Dtype | Cube (GEMM) | Vector (activation) | Notes |
|-------|-------------|---------------------|-------|
| fp16 (`half`) | Native Cube | Native Vector | Best throughput; primary tuning target |
| bf16 (`bfloat16`) | Native Cube (910B+) | Native Vector | Wider exponent; slightly lower mantissa precision |
| fp32 (`float`) | Cube with fp32 mode OR Vector fallback | Native Vector | May not saturate Cube; check CANN version |

**910B fp32 GEMM**: Cube supports fp32 matmul but peak TFLOPS is lower than fp16. For small M (decode), fp32 overhead is dominated by launch latency, not compute.

**fp32 activation-only ops**: Always run on Vector unit regardless of GEMM dtype.

## Template Kernel Pattern

```cpp
template <typename T>
__global__ __aicore__ void ffn_kernel(/* ... */) {
    AscendC::LocalTensor<T> buf = queue.AllocTensor<T>();
    AscendC::Matmul<T> mm;  // or dtype-specific MatmulImpl
    // ...
}

// Host launch dispatch:
extern "C" void launch_ffn(GM_ADDR x, /* ... */, int dtypeId, void* stream) {
    switch (dtypeId) {
        case 0: ffn_kernel<half><<<dim, nullptr, stream>>>(/* ... */); break;
        case 1: ffn_kernel<float><<<dim, nullptr, stream>>>(/* ... */); break;
        case 2: ffn_kernel<bfloat16_t><<<dim, nullptr, stream>>>(/* ... */); break;
    }
}
```

Use `half` (from `kernel_operator.h`), `float`, and `bfloat16_t` — verify exact typedef names in your CANN version's `kernel_operator.h`.

## pybind dtype Dispatch

```cpp
torch::Tensor ffn(const torch::Tensor& x, /* ... */) {
    auto dtype = x.scalar_type();
    if (dtype == torch::kFloat16) {
        launch_ffn_half(/* ... */);
    } else if (dtype == torch::kFloat32) {
        launch_ffn_float(/* ... */);
    } else if (dtype == torch::kBFloat16) {
        launch_ffn_bf16(/* ... */);
    } else {
        TORCH_CHECK(false, "unsupported dtype");
    }
    return torch::empty_like(x);  // pre-allocated output
}
```

Ensure `weight1`, `weight2`, and `x` share the same dtype — MKB test cases use consistent dtypes across inputs.

## Correctness Tolerances

MKB correctness check compares against reference `Model` (typically fp32 accumulation internally for npu_ffn).

| Candidate dtype | Reference | Typical tolerance |
|-----------------|-----------|-----------------|
| fp16 | fp16 baseline | atol ~1e-3, rtol ~1e-3 |
| bf16 | bf16 baseline | atol ~1e-2, rtol ~1e-2 |
| fp32 | fp32 baseline | atol ~1e-5, rtol ~1e-5 |

**SwiGLU / GELU**: gated activations amplify fp16 error — if correctness fails on swiglu cases only, check activation numerics (use hardware `Sigmoid` vs manual `Exp`).

## Mixed-Precision Strategies

### All-fp16/bf16 (Recommended for Speed)

Keep entire pipeline in 16-bit. Cube GEMM + Vector activation in same dtype.

### fp16 GEMM + fp32 Accumulation

Catlass / `Matmul` API supports fp32 accumulator with fp16 inputs. Use when correctness fails on large K dimensions:

```cpp
MatmulImpl<half, float> mm;  // A/B in half, accumulation in float
```

### fp32 I/O with fp16 Compute

Cast at boundaries only — rarely worth it for FFN; adds Vector cast overhead.

## dtype-Specific Pitfalls

| Issue | fp16 | bf16 | fp32 |
|-------|------|------|------|
| SwiGLU overflow in gate | possible for large inputs | less likely | rare |
| Cube NZ alignment | 16-element blocks | same | same |
| UB size pressure | 2 bytes/elem | 2 bytes/elem | 4 bytes/elem — halves tile size |
| Launch overhead dominates | M < 128 | M < 128 | M < 256 |

**fp32 UB OOM**: halve tile sizes vs fp16; see pattern-ub-oom.

## inner_precise Flag (Official — doc-torch-npu-npu-ffn)

| Value | Meaning | Effective for |
|-------|---------|---------------|
| 0 | High precision — internal **FP32** compute | fp16 only |
| 1 | High performance — internal **FP16** compute | fp16 only |

**Official rules**:
- **bf16** non-quant: `inner_precise` **must be 0**
- **fp16** non-quant: 0 or 1
- **int8** quant / pseudo-quant: 0 and 1 allowed but **ignored**

MKB test cases may pass `inner_precise` — check `get_input_groups()` and match reference behavior per case.

## Testing Strategy

1. Get one dtype compiling (fp16 easiest).
2. Add dtype dispatch in launch wrapper + pybind.
3. Run single-case debug before full 50-case sweep.
4. If bf16 fails but fp16 passes → check `bfloat16_t` typedef and Cube bf16 support flag.
5. If fp32 fails → verify Cube fp32 matmul path or fall back to Vector-based matmul for small sizes.

## Related Pages

- **kernel-ffn-fused-ascendc** — fused kernel using multi-dtype templates
- **lang-torch-npu-cpp-api** — pybind dispatch macros
- **pattern-precision-nan-debugging** — NaN/overflow diagnosis
- **technique-precision-tuning** — accumulation strategies
