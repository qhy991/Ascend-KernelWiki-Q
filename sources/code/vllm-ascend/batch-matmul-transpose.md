---
id: code-vllm-ascend-batch-matmul-transpose
title: vLLM Ascend Batch Matmul Transpose Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/batch_matmul_transpose
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/batch_matmul_transpose
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
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

# vLLM Ascend Batch Matmul Transpose Operator

vLLM Ascend batch-matmul-transpose custom operator showing how transposed layouts, tiling metadata, and Cube execution are packaged for serving workloads.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/batch_matmul_transpose`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/batch_matmul_transpose
