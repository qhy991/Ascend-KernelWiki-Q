---
id: code-vllm-ascend-ops
title: vLLM Ascend Operator Wrappers
type: source-code
repo: vllm-project/vllm-ascend
path: vllm_ascend/ops
url: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/ops
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- operator
- python
- torch-npu
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- global-memory
techniques:
- format-conversion
- kv-cache-paging
- pipeline-scheduling
kernel_types:
- matmul
- attention
- rope
- moe
languages:
- python
- cpp
---

# vLLM Ascend Operator Wrappers

vLLM Ascend operator wrapper source. It is evidence for Python-side dispatch to torch_npu and custom kernels, including format preparation, attention/MoE wrappers, and operator availability gates.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `vllm_ascend/ops`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/ops
