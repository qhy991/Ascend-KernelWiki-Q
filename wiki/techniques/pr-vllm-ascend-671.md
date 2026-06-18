---
id: technique-pr-vllm-ascend-671
title: "PR Insight: vllm-project/vllm-ascend #671"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek
  - attention
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/671"
---

# PR Insight: vllm-project/vllm-ascend #671

**Title:** [Fix] fix deepseek v0 attention eager mode

## Overview
This PR fixes DeepSeek v0 attention in eager mode by replacing the custom reshape_and_cache_siso operator with PyTorch operation combinations due to functionality issues with the custom op.

## Technical Significance
Custom operators can have edge case bugs. Falling back to PyTorch ops ensures correctness while the custom op is being fixed. This is a temporary workaround for DeepSeek v0 eager mode.

## Related
- kernel-attention
- technique-deepseek