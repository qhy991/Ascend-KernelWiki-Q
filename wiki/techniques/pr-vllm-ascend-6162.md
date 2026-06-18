---
id: technique-pr-vllm-ascend-6162
title: "PR Insight: vllm-project/vllm-ascend #6162"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eagle
  - spec-decode
  - dp
  - hccl-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6162"
---

# PR Insight: vllm-project/vllm-ascend #6162

**Title:** [v0.13.0]skip eagle dp allreduce

## Overview
This PR optimizes Eagle speculative decoding by skipping DP allreduce operations for dense draft models. Since dense draft models don't require communication between data parallel groups, the num_tokens_across_dp allreduce can be skipped to improve performance. The changes affect the eagle proposer and model runner on the v0.13.0 branch.

## Technical Significance
Eagle spec decoding uses draft models to predict candidate tokens. For dense draft heads, there's no cross-DP communication needed for token counting. Skipping the allreduce reduces communication overhead significantly, improving speculative decoding throughput. This optimization is specific to the v0.13.0 branch's dense-only Eagle implementation.

## Related
- `technique-spec-decode`, `technique-hccl-optimization`, `technique-eagle`