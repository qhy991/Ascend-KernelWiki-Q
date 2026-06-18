---
id: technique-pr-vllm-ascend-18
title: "PR Insight: vllm-project/vllm-ascend #18"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - operator-fusion
  - attention
  - rope
  - elementwise
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/18"
---

# PR Insight: vllm-project/vllm-ascend #18

**Title:** [Hardware][Ascend] Add silu_and_mul/rope; Add mix ops into attention layer

## Overview
This PR adds silu_and_mul activation and rope (rotary positional embedding) operators, then refactors the attention layer to use three fused operators: reshape_and_cache, pagedattention, and selfattention. The changes reduce attention.py from 305 deletions to 188 additions, streamlining the implementation.

## Technical Significance
This is a performance-critical refactor that replaces generic operator sequences with Ascend-specific fused operators. Fusing reshape_and_cache with attention operations reduces memory movement and improves cache locality. The silu_and_mul and rope ops are common activation and positional encoding components in transformer models.

## Related
- kernel-attention
- technique-operator-fusion
- technique-rope