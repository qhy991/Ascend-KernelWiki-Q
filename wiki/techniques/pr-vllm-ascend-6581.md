---
id: technique-pr-vllm-ascend-6581
title: "PR Insight: vllm-project/vllm-ascend #6581"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rotary-embedding
  - partial-rope
  - bugfix
  - compatibility
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6581"
---

# PR Insight: vllm-project/vllm-ascend #6581

**Title:** [BugFix] Add support for rotary_dim parameter when using partial rope in rotary_embedding

## Overview
This PR adds support for the rotary_dim parameter in rotary embedding operations for models using partial RoPE (rotary position embedding). Previously, only partial_rotary_factor was supported, causing tensor size mismatch errors for models like Ling-1T that use rotary_dim in config.json.

## Technical Significance
Fixes compatibility issues with models that specify partial RoPE using rotary_dim instead of partial_rotary_factor. The fix ensures proper rope_dim calculation to prevent tensor size mismatch errors during attention computation.

## Related
- `kernel-attention`