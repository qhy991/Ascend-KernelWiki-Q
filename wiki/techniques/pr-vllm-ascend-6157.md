---
id: technique-pr-vllm-ascend-6157
title: "PR Insight: vllm-project/vllm-ascend #6157"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - memory-alignment
  - hbm
  - synchronization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6157"
---

# PR Insight: vllm-project/vllm-ascend #6157

**Title:** [0.13.0][BugFix]bug fix for dispatch_ffn_combine

## Overview
This PR cherry-picks the dispatch_ffn_combine synchronization fix from PR #6156 to the v0.13.0 branch. The fix pads synchronization data to 512B alignment to match Ascend A3's HBM atomic write behavior for expertPerRank configurations that don't naturally align to 512B.

## Technical Significance
This backport ensures v0.13.0 users receive the synchronization fix without waiting for the next major release. The padding ensures correct synchronization checking when EP * expertPerRank doesn't naturally align to 512B boundaries, preventing race conditions in MoE routing for non-DeepSeek configurations.

## Related
- `technique-moe`, `technique-memory-alignment`, `technique-hbm`, `technique-synchronization`