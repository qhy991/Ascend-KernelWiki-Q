---
id: technique-pr-vllm-ascend-4857
title: "PR Insight: vllm-project/vllm-ascend #4857"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3
  - w8a8
  - data-parallel
  - test-skip
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4857"
---

# PR Insight: vllm-project/vllm-ascend #4857

**Title:** [Test] Temporarily skips Qwen3-30B-A3B-W8A8 data parallel test case

## Overview
This PR temporarily skips the Qwen3-30B-A3B-W8A8 data parallel test case due to CI failures. The skip is applied to tests/e2e/multicard/test_data_parallel.py.

## Technical Significance
Test stability measure to unblock CI while the underlying issue with W8A8 quantized Qwen3-30B in data parallel mode is being investigated.

## Related
- `technique-w8a8-quantization`
- `technique-data-parallelism`
- `kernel-qwen3`