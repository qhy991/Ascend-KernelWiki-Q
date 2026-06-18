---
id: technique-pr-vllm-ascend-2744
title: "PR Insight: vllm-project/vllm-ascend #2744"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - rope
  - deepseek
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2744"
---

# PR Insight: vllm-project/vllm-ascend #2744

**Title:** [bugfix] fix deepseek rope sincoscache re-generation

## Overview
This PR fixes a bug where `sin_cos_cache` in rotary embedding (RoPE) was being redundantly regenerated when `kv_seqlen` exceeded 4k tokens. The issue occurred because the cache initialization was limited to 4k tokens, causing repeated cache regeneration for longer sequences.

## Technical Significance
Eliminating redundant cache regeneration improves performance for long-context DeepSeek models. The fix reduces computational overhead and memory allocation in the forward pass, particularly beneficial for inference with long sequences on Ascend NPU.

## Related
- `kernel-rotary-embedding`
- `kernel-deepseek-rope`
- `technique-cache-optimization`
- `technique-long-context`