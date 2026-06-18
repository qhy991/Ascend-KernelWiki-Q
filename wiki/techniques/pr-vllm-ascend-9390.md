---
id: technique-pr-vllm-ascend-9390
title: "PR Insight: vllm-project/vllm-ascend #9390"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - dsa
  - index-cache
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9390"
---

# PR Insight: vllm-project/vllm-ascend #9390

**Title:** [Feature] IndexCache: reuse topk_indices across decode steps for DSA models (DeepSeek V4)

## Overview
This PR implements IndexCache optimization for DSA (DeepSeek Sparse Attention) models, allowing topk_indices to be reused across decode steps. The changes affect DSA attention implementation, model code, and operator logic to cache and reuse index selections.

## Technical Significance
Reusing topk_indices eliminates redundant computation across decode steps, significantly reducing CPU overhead and improving inference throughput. This optimization is particularly impactful for sparse attention patterns where index selection is a major component of the computation.

## Related
- `kernel-attention`
- `technique-data-reuse`
- `kernel-flash-attention`