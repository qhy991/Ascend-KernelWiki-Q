---
id: code-vllm-ascend-model-runner
title: vLLM Ascend Model Runner
type: source-code
repo: vllm-project/vllm-ascend
path: vllm_ascend/worker
url: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/worker
source_category: upstream-code
architectures:
- ascend910b
tags:
- vllm
- scheduler
- inference
- python
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- global-memory
- cube-unit
- vector-unit
techniques:
- kv-cache-paging
- pipeline-scheduling
- tensor-parallel-overlap
kernel_types:
- attention
- matmul
- moe
languages:
- python
---

# vLLM Ascend Model Runner

vLLM Ascend worker/model-runner source. This path is evidence for request scheduling, execution orchestration, KV-cache management, and how Python control flow invokes NPU kernels in serving.

## Code Location

- Repository: `vllm-project/vllm-ascend`
- Path: `vllm_ascend/worker`
- URL: https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/worker
