---
id: code-vllm-ascend-inplace-partial-rotary
title: vLLM Ascend In-place Partial Rotary Operator
type: source-code
repo: vllm-project/vllm-ascend
path: csrc/attention/inplace_partial_rotary_mul
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/inplace_partial_rotary_mul
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- rope
- attention
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- vector-unit
- unified-buffer
- global-memory
techniques:
- data-reuse
- pipeline-scheduling
kernel_types:
- rope
- attention
- elementwise
languages:
- cpp
- ascendc
---

# vLLM Ascend In-place Partial Rotary Operator

vLLM Ascend rotary-position operator used as code evidence for in-place vector transformations on query/key tensors during inference.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc/attention/inplace_partial_rotary_mul`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc/attention/inplace_partial_rotary_mul
