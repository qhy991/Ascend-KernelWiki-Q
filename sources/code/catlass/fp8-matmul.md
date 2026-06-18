---
id: code-catlass-fp8-matmul
title: CATLASS FP8 Matmul Example
type: source-code
repo: Ascend/catlass
path: examples/29_a2_fp8_e4m3_matmul
url: https://gitee.com/ascend/catlass/tree/master/examples/29_a2_fp8_e4m3_matmul
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- fp8
- quantization
- matmul
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- l1-buffer
- l0-buffer
techniques:
- quantization-int8
- tiling-strategy
- pipeline-scheduling
kernel_types:
- quant-matmul
- matmul
- gemm
languages:
- cpp
- ascendc
---

# CATLASS FP8 Matmul Example

CATLASS FP8 E4M3 matmul example documenting low-precision GEMM structure and scale-aware data preparation for Ascend accelerator kernels.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/29_a2_fp8_e4m3_matmul`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/29_a2_fp8_e4m3_matmul
