---
id: code-vllm-ascend-attention
title: vLLM Ascend Attention Backend
type: source-code
repo: vllm-project/vllm-ascend
path: vllm_ascend/attention
url: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/attention
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- attention
- paged-attention
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- global-memory
- unified-buffer
techniques:
- kv-cache-paging
- online-softmax
- pipeline-scheduling
kernel_types:
- attention
- paged-attention
- flash-attention
languages:
- python
- cpp
- ascendc
---

# vLLM Ascend Attention Backend

vLLM Ascend attention backend source. It anchors evidence for how vLLM's paged attention abstractions map onto Ascend NPU operators and custom kernels in serving workloads.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `vllm_ascend/attention`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/attention
