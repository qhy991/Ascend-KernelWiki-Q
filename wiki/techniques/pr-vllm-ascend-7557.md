---
id: technique-pr-vllm-ascend-7557
title: "PR Insight: vllm-project/vllm-ascend #7557"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gmm
  - moe
  - accuracy
  - reversion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7557"
---

# PR Insight: vllm-project/vllm-ascend #7557

**Title:** Revert "GMM custom operator optimization in small batch scenarios (vllm-project#7100)"

## Overview
This PR reverts a GMM custom operator optimization for small batch scenarios because it caused accuracy degradation for Qwen3Next (GSM8k: 98 -> 91). The reversion restores the previous implementation to maintain correctness.

## Technical Significance
This reversion matters for MoE inference accuracy on Ascend. The original optimization improved performance for small batches but introduced numerical inaccuracies. Accuracy is critical for LLM applications, so the optimization was reverted to ensure correct results. This highlights the importance of comprehensive accuracy testing for performance optimizations.

## Related
- technique-moe
- technique-accuracy-testing