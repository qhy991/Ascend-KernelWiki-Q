---
id: code-catlass-quant-matmul
title: CATLASS Quantized Matmul Example
type: source-code
repo: Ascend/catlass
path: examples/12_quant_matmul
url: https://gitee.com/ascend/catlass/tree/master/examples/12_quant_matmul
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- quantization
- matmul
- ascendc
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- nz-format
- l0-buffer
techniques:
- quantization-int8
- nz-tiling
- format-conversion
kernel_types:
- quant-matmul
- matmul
- gemm
languages:
- cpp
- ascendc
---

# CATLASS Quantized Matmul Example

CATLASS quantized matmul example for low-precision GEMM flows, including quantized operands, Cube execution, and vector-side scale/dequantization handling.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/12_quant_matmul`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/12_quant_matmul
