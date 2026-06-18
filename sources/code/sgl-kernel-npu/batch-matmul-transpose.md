---
id: code-sgl-kernel-npu-batch-matmul-transpose
title: SGL Kernel NPU Batch Matmul Transpose Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/batch_matmul_transpose
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/batch_matmul_transpose
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- matmul
- transpose
- ascendc
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- nz-format
- global-memory
techniques:
- format-conversion
- tiling-strategy
- pipeline-scheduling
kernel_types:
- matmul
- gemm
languages:
- cpp
- ascendc
---

# SGL Kernel NPU Batch Matmul Transpose Operator

SGL Kernel NPU batch matmul transpose operator with host tiling and kernel directories, anchoring GEMM layout-transform evidence.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/batch_matmul_transpose`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/batch_matmul_transpose
