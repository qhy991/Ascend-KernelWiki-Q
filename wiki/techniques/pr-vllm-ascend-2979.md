---
id: technique-pr-vllm-ascend-2979
title: "PR Insight: vllm-project/vllm-ascend #2979"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decoding
  - eagle
  - concurrency
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2979"
---

# PR Insight: vllm-project/vllm-ascend #2979

**Title:** [Bugfix] eagle and eagle3 spec decode failures and enable e2e test

## Overview
This PR fixes Eagle and Eagle3 speculative decoding failures, adapts to scenarios where speculative tokens exceed 2, and improves draft model acceptance rates under high concurrency. It enables end-to-end testing for these speculative decoding implementations.

## Technical Significance
The fixes address correctness and performance issues in Eagle-based speculative decoding. The high concurrency improvements and support for more than 2 speculative tokens enhance the practicality of speculative decoding for production workloads, improving overall inference throughput.

## Related
- `technique-spec-decoding`, `kernel-eagle-ascendc`, `technique-concurrency-optimization`