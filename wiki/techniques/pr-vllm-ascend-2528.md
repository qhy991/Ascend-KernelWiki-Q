---
id: technique-pr-vllm-ascend-2528
title: "PR Insight: vllm-project/vllm-ascend #2528"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - sliding-window
  - gemma3
  - feature
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2528"
---

# PR Insight: vllm-project/vllm-ascend #2528

**Title:** [Feat]attention add sliding windows size

## Overview
This PR adds a sliding window size parameter to attention for models like Gemma3. The implementation modifies `vllm_ascend/attention/attention_v1.py` (79 lines added, 19 lines deleted) and adds comprehensive tests to support sliding window attention patterns.

## Technical Significance
This feature enables efficient processing of long sequences using sliding window attention, which only attends to recent tokens rather than the full context. This reduces computational complexity from O(n²) to O(n*k) where k is the window size, enabling more efficient processing of very long sequences.

## Related
- `kernel-attention-v1`, `kernel-attention-ascendc`, `technique-sliding-window`, `technique-long-context`