---
id: technique-pr-vllm-ascend-7861
title: "PR Insight: vllm-project/vllm-ascend #7861"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - inference
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7861"
---

# PR Insight: vllm-project/vllm-ascend #7861

**Title:** [BugFix] Fix spec decode + logprobs crash when async scheduling is disabled

## Overview
This PR fixes a TypeError crash that occurs when logprobs is enabled with speculative decoding on NPU under synchronous scheduling. The bug was caused by incorrectly assigning the second return value from `RejectionSampler.parse_output()` to `cu_num_tokens` and passing it to `logprobs_tensors.tolists()`. The fix splits logprobs handling into two paths based on `max_gen_len`.

## Technical Significance
Speculative decoding is a key optimization for inference throughput. The crash affected multiple speculative decoding methods including suffix, ngram, and MTP/Eagle3 when async scheduling was manually disabled. The fix ensures correct type handling for logprobs tensors, preventing crashes and enabling proper logprobs computation with speculative decoding on NPU.

## Related
- `kernel-attention`
- `pattern-speculative-decoding`
- `technique-inference-optimization`