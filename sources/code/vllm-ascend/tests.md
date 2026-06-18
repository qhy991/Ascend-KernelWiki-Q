---
id: code-vllm-ascend-tests
title: vLLM Ascend Kernel and Backend Tests
type: source-code
repo: vllm-project/vllm-ascend
path: tests
url: https://github.com/vllm-project/vllm-ascend/tree/main/tests
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- tests
- inference
- python
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- global-memory
techniques:
- kv-cache-paging
- format-conversion
kernel_types:
- attention
- matmul
- moe
- rope
languages:
- python
---

# vLLM Ascend Kernel and Backend Tests

vLLM Ascend test suite source. These tests provide executable evidence for NPU backend behavior, custom kernel correctness, model execution, and regression coverage around serving workloads.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `tests`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/tests
