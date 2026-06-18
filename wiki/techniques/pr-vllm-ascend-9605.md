---
id: technique-pr-vllm-ascend-9605
title: "PR Insight: vllm-project/vllm-ascend #9605"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - mtp
  - acceptance
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9605"
---

# PR Insight: vllm-project/vllm-ascend #9605

**Title:** [BugFix] Fix dsv4 mtp acceptance

## Overview
This PR fixes an issue with MTP (Multi-Token Prediction) acceptance rates in DeepSeek V4. The fix is implemented in the DSA v1 attention implementation to ensure proper token acceptance behavior.

## Technical Significance
MTP acceptance rate is a key metric for speculative decoding efficiency. Low acceptance rates reduce the effectiveness of the optimization. The fix improves acceptance rates, ensuring that MTP provides the expected performance benefits for DeepSeek V4 models.

## Related
- `kernel-attention`
- `technique-spec-decode`