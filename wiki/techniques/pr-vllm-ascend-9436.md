---
id: technique-pr-vllm-ascend-9436
title: "PR Insight: vllm-project/vllm-ascend #9436"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - flashcomm1
  - mtp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9436"
---

# PR Insight: vllm-project/vllm-ascend #9436

**Title:** [BugFix][Model] Fix NaN hidden states and low MTP acceptance rate when FlashComm1 is enabled

## Overview
This PR fixes NaN hidden states and low MTP (Multi-Token Prediction) acceptance rate issues that occur when FlashComm1 is enabled. The fix is implemented in the DeepSeek V4 model code to ensure proper numerical behavior with FlashComm1 communication optimizations.

## Technical Significance
FlashComm1 is a communication optimization that can affect numerical behavior if not handled correctly. The fix prevents NaN propagation and improves MTP acceptance rates, ensuring both correctness and performance when using FlashComm1 optimizations.

## Related
- `kernel-attention`
- `technique-hccl-optimization`