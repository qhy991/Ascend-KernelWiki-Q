---
id: technique-pr-vllm-ascend-6310
title: "PR Insight: vllm-project/vllm-ascend #6310"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - rotary-embedding
  - attention
  - rope
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6310"
---

# PR Insight: vllm-project/vllm-ascend #6310

**Title:** [Bugfix]Modify NPU rotary encoding parameter fields，fix RopeOperation setup failed in condition of self.rotary_dim < self.head_size

## Overview
This PR fixes a bug in rotary embedding parameter configuration where `self.head_size` was incorrectly used instead of `self.rotary_dim` when setting up the RopeOperation. The fix ensures correct dimension handling for models where rotary_dim < head_size.

## Technical Significance
The bug caused RopeOperation setup failures in models with partial rotary embeddings (where only a portion of the head dimension uses rotary encoding). The fix ensures proper parameterization by using the correct rotary dimension rather than the full head size.

## Related
- `technique-rotary-embedding`
- `technique-attention`
- `technique-rope`