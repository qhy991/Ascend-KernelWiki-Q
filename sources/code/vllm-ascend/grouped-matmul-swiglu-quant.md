---
id: code-vllm-ascend-grouped-matmul-swiglu-quant
title: vLLM Ascend Grouped Matmul SwiGLU Quant Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/gmm/grouped_matmul_swiglu_quant
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/gmm/grouped_matmul_swiglu_quant
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- grouped-gemm
- swiglu
- quantization
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
- cube-vector-overlap
- pipeline-scheduling
kernel_types:
- grouped-gemm
- moe
- swiglu
- quant-matmul
languages:
- cpp
- ascendc
---

# vLLM Ascend Grouped Matmul SwiGLU Quant Operator

vLLM Ascend grouped matmul plus SwiGLU quant operator, serving as code evidence for MoE MLP fusion and low-precision grouped GEMM.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/gmm/grouped_matmul_swiglu_quant`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/gmm/grouped_matmul_swiglu_quant
