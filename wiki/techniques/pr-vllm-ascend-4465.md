---
id: technique-pr-vllm-ascend-4465
title: "PR Insight: vllm-project/vllm-ascend #4465"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - mtp
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4465"
---

# PR Insight: vllm-project/vllm-ascend #4465

**Title:** [Feat] MTP support DeepSeekV3.2

**Author:** ZYang6263 | **Merged:** 2025-12-03

## Overview
Adds new functionality for  operations. The feature enhances model capabilities and performance.

## Technical Significance
KV cache management is critical for long-context inference and memory efficiency. Changes here improve memory utilization and enable better paging strategies, directly affecting the maximum supported sequence length and throughput.

## Related
- `technique-kv-cache-paging`
