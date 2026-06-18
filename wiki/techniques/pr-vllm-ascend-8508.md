---
id: technique-pr-vllm-ascend-8508
title: "PR Insight: vllm-project/vllm-ascend #8508"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - sliding-window
  - bugfix
  - block-tables
  - sparse-mode
  - fia
  - throughput
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8508"
---

# PR Insight: vllm-project/vllm-ascend #8508

**Title:** [BugFix] Fix sliding window attention computation and improve throughput

## Overview
This PR fixes critical issues in sliding window attention implementation: output corruption in full-graph replay path due to block_tables rebinding, and repetition issues with sparse_mode=3 and _forward_fia_slidingwindow. The fix keeps captured block_tables for SWA models, uses sparse_mode=4 with proper parameters, adds sliding window support in graph capture mode, and consolidates SWA handling into unified TND layout path.

## Technical Significance
Sliding window attention is critical for long-context models, and these fixes ensure correct and efficient computation. The block_tables handling fix prevents output corruption, while the sparse_mode and parameter fixes eliminate repetition issues. Adding graph capture support for SWA enables performance optimizations for long-context inference scenarios.

## Related
- `technique-sliding-window-attention`
- `technique-graph-mode`
- `technique-block-tables`