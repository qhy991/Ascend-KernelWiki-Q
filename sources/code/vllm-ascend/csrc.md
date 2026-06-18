---
id: code-vllm-ascend-csrc
title: vLLM Ascend C++/AscendC Extension Source
type: source-code
repo: vllm-project/vllm-ascend
path: csrc
url: https://github.com/vllm-project/vllm-ascend/tree/main/csrc
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- ascendc
- cpp
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- vector-unit
- unified-buffer
- mte
- global-memory
techniques:
- pipeline-scheduling
- kv-cache-paging
kernel_types:
- attention
- rope
- elementwise
languages:
- cpp
- ascendc
- python
---

# vLLM Ascend C++/AscendC Extension Source

vLLM Ascend native extension source tree. It is code evidence for binding custom NPU kernels into vLLM, including C++ extension build logic, torch operator registration, and AscendC kernel integration.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `csrc`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/csrc
