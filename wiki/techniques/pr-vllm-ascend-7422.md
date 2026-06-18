---
id: technique-pr-vllm-ascend-7422
title: "PR Insight: vllm-project/vllm-ascend #7422"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-next
  - hybrid-attention
  - context-parallelism
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7422"
---

# PR Insight: vllm-project/vllm-ascend #7422

**Title:** [main][Attention][Feature] Add support for Qwen3-next hybrid attention in piecewise & full_decode_only

## Overview
This PR adds support for Qwen3-next's hybrid attention mechanism in context parallelism and graph mode execution. Changes include passing new metadata for padded tokens in flash attention, refactoring QKV tensor preparation for hybrid attention, adding support for multiple KV cache groups, and updating CP utilities for token splitting and metadata generation.

## Technical Significance
This support matters for Qwen3-next inference efficiency on Ascend. Hybrid attention combines different attention patterns that require specialized handling in CP and graph modes. The metadata updates and QKV refactoring enable correct token distribution and cache management across context parallel ranks, unlocking performance gains for this new model architecture.

## Related
- technique-context-parallelism
- technique-hybrid-attention
- technique-graph-mode