---
id: code-catlass-w8a16-matmul
title: CATLASS W8A16 Matmul Example
type: source-code
repo: Ascend/catlass
path: examples/30_w8a16_matmul
url: https://gitee.com/ascend/catlass/tree/master/examples/30_w8a16_matmul
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- w8a16
- quantization
- matmul
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
- format-conversion
- nz-tiling
kernel_types:
- quant-matmul
- matmul
- gemm
languages:
- cpp
- ascendc
---

# CATLASS W8A16 Matmul Example

CATLASS W8A16 matmul example used as source evidence for weight-only quantized GEMM and the related layout, scale, and epilogue requirements.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/30_w8a16_matmul`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/30_w8a16_matmul
