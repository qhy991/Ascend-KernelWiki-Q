---
id: technique-pr-vllm-ascend-1399
title: "PR Insight: vllm-project/vllm-ascend #1399"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - rotary-embedding
  - ci
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1399"
---

# PR Insight: vllm-project/vllm-ascend #1399

**Title:** [Bugfix] Sync MRotaryEmbedding interface change to recover CI

## Overview
This PR synchronizes the MRotaryEmbedding interface with upstream changes to restore CI pipeline functionality.

## Technical Significance
Restores CI stability by updating MRotaryEmbedding to match vLLM's API changes. The fix ensures that rotary embedding operations work correctly in V1 model runner, which is critical for maintaining test coverage across all rotary embedding variants.

## Related
- `technique-rotary-embedding`
- `kernel-attention`