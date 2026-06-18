---
id: code-sgl-kernel-npu-catlass
title: SGL Kernel NPU CATLASS Utility Kernels
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/catlass
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/catlass
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- catlass
- matmul
- fp8
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
- nz-tiling
- pipeline-scheduling
kernel_types:
- matmul
- gemm
- quant-matmul
languages:
- cpp
- ascendc
---

# SGL Kernel NPU CATLASS Utility Kernels

SGL Kernel NPU CATLASS-backed source tree, including GEMM utility code and low-precision matmul components for production inference.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/catlass`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/catlass
