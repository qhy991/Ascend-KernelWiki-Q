---
id: code-catlass-batched-matmul
title: CATLASS Batched Matmul Example
type: source-code
repo: Ascend/catlass
path: examples/01_batched_matmul
url: https://gitee.com/ascend/catlass/tree/master/examples/01_batched_matmul
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- batched-matmul
- gemm
- ascendc
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- l1-buffer
- l0-buffer
- nz-format
techniques:
- nz-tiling
- pipeline-scheduling
- double-buffering
kernel_types:
- matmul
- gemm
languages:
- cpp
- ascendc
---

# CATLASS Batched Matmul Example

CATLASS batched matmul example showing how the GEMM template stack handles a batch dimension while preserving Cube-friendly operand layouts and tiled scheduling.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/01_batched_matmul`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/01_batched_matmul
