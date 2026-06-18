---
id: code-vllm-ascend-kv-quant-sparse-attn
title: vLLM Ascend KV Quant Sparse Attention Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/attention/kv_quant_sparse_attn_sharedkv
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/kv_quant_sparse_attn_sharedkv
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- sparse-attention
- kv-cache
- quantization
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- unified-buffer
- global-memory
techniques:
- kv-cache-paging
- quantization-int8
- online-softmax
kernel_types:
- attention
- paged-attention
- quant-matmul
languages:
- cpp
- ascendc
---

# vLLM Ascend KV Quant Sparse Attention Operator

vLLM Ascend sparse attention operator over quantized shared KV data, anchoring code evidence for compressed cache reads and quantized attention execution.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/attention/kv_quant_sparse_attn_sharedkv`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/kv_quant_sparse_attn_sharedkv
