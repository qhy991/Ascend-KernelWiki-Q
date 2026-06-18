---
id: code-vllm-ascend-compressor
title: vLLM Ascend Attention Compressor Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/attention/compressor
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/compressor
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- attention
- compressor
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- vector-unit
- unified-buffer
- global-memory
techniques:
- kv-cache-paging
- data-reuse
- pipeline-scheduling
kernel_types:
- attention
- elementwise
languages:
- cpp
- ascendc
---

# vLLM Ascend Attention Compressor Operator

vLLM Ascend compressor custom operator with host and kernel directories, useful as code evidence for attention-side compression and cache preprocessing.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/attention/compressor`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/compressor
