---
id: technique-pr-vllm-ascend-9545
title: "PR Insight: vllm-project/vllm-ascend #9545"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - reduce-sampling
  - spec-decode
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9545"
---

# PR Insight: vllm-project/vllm-ascend #9545

**Title:** [BugFix] fix reduce_sampling

## Overview
This PR fixes an issue with the reduce_sampling operation used in speculative decoding. The changes affect the rejection sampler, spec decode proposer, worker model runner, and platform-specific patches.

## Technical Significance
Reduce sampling is a critical component of speculative decoding that combines multiple candidate tokens. The fix ensures correct sampling behavior, preventing incorrect token generation and improving the reliability of speculative decoding optimizations.

## Related
- `technique-spec-decode`