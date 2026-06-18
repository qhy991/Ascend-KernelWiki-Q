---
id: code-vllm-ascend-sparse-flash-attention
title: vLLM Ascend Sparse Flash Attention Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/attention/sparse_flash_attention
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/sparse_flash_attention
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- sparse-attention
- flash-attention
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- unified-buffer
- global-memory
techniques:
- online-softmax
- kv-cache-paging
- pipeline-scheduling
kernel_types:
- attention
- flash-attention
- paged-attention
languages:
- cpp
- ascendc
---

# vLLM Ascend Sparse Flash Attention Operator

vLLM Ascend sparse FlashAttention source directory with host/kernel code and examples, useful for mining sparse attention scheduling and softmax patterns.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/attention/sparse_flash_attention`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/sparse_flash_attention
