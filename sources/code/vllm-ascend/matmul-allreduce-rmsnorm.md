---
id: code-vllm-ascend-matmul-allreduce-rmsnorm
title: vLLM Ascend Matmul AllReduce Add RMSNorm Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/mc2/matmul_allreduce_add_rmsnorm
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/mc2/matmul_allreduce_add_rmsnorm
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- matmul
- allreduce
- rmsnorm
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- hccs
- global-memory
techniques:
- tensor-parallel-overlap
- hccl-optimization
- cube-vector-overlap
kernel_types:
- matmul
- gemm
- rmsnorm
languages:
- cpp
- ascendc
---

# vLLM Ascend Matmul AllReduce Add RMSNorm Operator

vLLM Ascend MC2 operator fusing matmul, communication, residual add, and RMSNorm; it is source evidence for tensor-parallel overlap around NPU GEMM.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/mc2/matmul_allreduce_add_rmsnorm`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/mc2/matmul_allreduce_add_rmsnorm
