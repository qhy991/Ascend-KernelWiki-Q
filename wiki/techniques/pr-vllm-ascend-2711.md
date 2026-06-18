---
id: technique-pr-vllm-ascend-2711
title: "PR Insight: vllm-project/vllm-ascend #2711"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - chunked-prefill
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2711"
---

# PR Insight: vllm-project/vllm-ascend #2711

**Title:** fix : support chunked_prefill with deepseek_mtp

## Overview
This PR adds support for chunked prefill operations when using DeepSeek MTP (Multi-Token Prediction). The fix enables efficient processing of long input sequences while maintaining the performance benefits of MTP in distributed inference scenarios.

## Technical Significance
Chunked prefill is essential for handling long-context inputs efficiently. Combining it with MTP provides both throughput and latency benefits for production workloads, particularly for DeepSeek models with long context windows on Ascend NPU.

## Related
- `technique-mtp`
- `technique-chunked-prefill`
- `kernel-deepseek-mtp`
- `technique-long-context`