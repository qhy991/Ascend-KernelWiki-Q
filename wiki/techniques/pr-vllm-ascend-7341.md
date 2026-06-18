---
id: technique-pr-vllm-ascend-7341
title: "PR Insight: vllm-project/vllm-ascend #7341"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v3.2
  - rotary-embedding
  - accuracy
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7341"
---

# PR Insight: vllm-project/vllm-ascend #7341

**Title:** [bugfix][accuracy] Fix ds indexer accuracy problem caused by k rope

## Overview
This PR fixes an accuracy bug in DeepSeek V3.2 where the rotary embedding algorithm in the indexer should use Neox-style instead of GPTJ-style. PR #4641 originally fixed this, but PR #5701 accidentally removed the fix. This PR restores the correct Neox-style rotary embedding implementation.

## Technical Significance
This fix matters for DeepSeek V3.2 inference accuracy on Ascend. Rotary embedding style (Neox vs GPTJ) determines how position information is applied to query/key tensors. Using the wrong style causes incorrect attention computation and degraded model output quality. The fix ensures correct rotary position encoding for DeepSeek's attention mechanism.

## Related
- technique-attention
- pattern-rotary-embedding