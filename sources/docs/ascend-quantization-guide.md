---
id: doc-ascend-quantization-guide
title: "Ascend Quantization — FP8/INT8 Operator Development"
type: source-doc
architectures: [ascend910b]
tags: [quantization, fp8, int8, ascendc]
date: '2026-03-01'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/Ascendcopdevg/atlas_ascendc_10_0042.html
hardware_features: [cube-unit, vector-unit]
techniques: [nz-tiling]
confidence: verified
---

# Ascend Quantization Guide

Official CANN documentation for developing quantized operators on Ascend 910B, covering FP8 and INT8 computation with AscendC.

## Key Content

### FP8 Support (Ascend 910B Only)

- **Formats**: E4M3 (for weights) and E5M2 (for gradients/activations)
- **Cube Unit**: Supports FP8 input with FP32 accumulation (analogous to NVIDIA H100 FP8 Tensor Cores)
- **Performance**: ~2× throughput improvement over FP16 for matrix multiplication

### INT8 Vector Operations

- INT8 element-wise operations on Vector unit
- Dequantization patterns: INT8 → FP16/FP32 before epilogue operations
- Scale and zero-point handling in UB

### AscendC Quantization API

```ascendc
// FP8 Matmul example
Matmul(fp8_A_nz, fp8_B_nz, fp32_C_nz, M, N, K, 
       scale_A, scale_B, scale_C);  // Per-channel scales

// INT8 Vector dequantization
DataCopy(int8_input, fp32_buffer, size, INT8_TO_FP32, scale);
```

### Integration Frameworks

- **MindSpore**: QAT and PTQ workflows with Ascend quantization-aware operators
- **PyTorch**: Ascend PTQ tools for model quantization
- **ONNX**: Quantized operator import/export support

## Performance Claims

- FP8 GEMM: Up to 640 TFLOPS on Ascend 910B (theoretical peak)
- INT8 Vector: Up to 128 TOPS per AICore
- Memory bandwidth savings: 50% reduction compared to FP16

## Developer Guidance

Document provides:
1. Quantization parameter tuning guidelines
2. Accuracy preservation strategies
3. Hybrid precision patterns (FP8 compute, FP16 master weights)
4. Debugging quantization accuracy issues

## Hardware Requirements

- FP8 operations require Ascend 910B (not supported on 910A)
- INT8 supported on both 910A and 910B
- Requires CANN 8.0.RC3 or later

## Related Resources

- [Catlass Quantized GEMM Templates](kernel-matmul-ascendc)
- [NZ Format for Quantized Data](pattern-nz-format-traps)
- [Operator Fusion with Quantization](doc-ascend-operator-fusion)
