---
id: technique-pr-vllm-ascend-1266
title: "PR Insight: vllm-project/vllm-ascend #1266"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - rotary-embedding
  - bugfix
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1266"
---

# PR Insight: vllm-project/vllm-ascend #1266

**Title:** [BugFix] fix length of sin/cos cache in rope

## Overview
This PR fixes a bug in the rotary embedding (RoPE) implementation where the sin/cos cache was constructed shorter than the model's max positional embedding. The fix ensures the cache allocation matches the full positional embedding dimensions.

## Technical Significance
Corrects RoPE cache allocation to prevent out-of-bounds access during inference with long sequences. The bug manifested when positional embeddings exceeded the pre-allocated cache size, causing incorrect rotation calculations and potential crashes. The fix is localized to `vllm_ascend/ops/rotary_embedding.py`, ensuring proper dimensionality for rotary position encoding computations.

## Related
- `technique-rotary-embedding`
- `kernel-attention`