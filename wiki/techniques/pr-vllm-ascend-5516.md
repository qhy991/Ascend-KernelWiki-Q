---
id: technique-pr-vllm-ascend-5516
title: "PR Insight: vllm-project/vllm-ascend #5516"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - mla
  - bugfix
  - moonlight
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5516"
---

# PR Insight: vllm-project/vllm-ascend #5516

**Title:** [Bugfix] record cos and sin cache in AscendRotaryEmbedding

## Overview
This PR fixes a bug where `_cos_cache` and `_sin_cache` were not recorded correctly in `AscendRotaryEmbedding` for models like Moonlight that use MLA (Multi-Head Latent Attention) but don't have `rope_scaling` in their config.json. The fix ensures proper cache recording for all RoPE scenarios.

## Technical Significance
Correct cos and sin cache recording is essential for RoPE operation correctness, particularly in MLA attention scenarios. This bug fix ensures models without explicit rope_scaling configurations can still properly utilize RoPE embeddings on Ascend NPU, preventing inference errors in edge cases.

## Related
- `kernel-attention` (MLA and RoPE integration)
- `technique-rope` (Rotary Positional Embeddings)
- `technique-moonlight` (Moonlight model support)