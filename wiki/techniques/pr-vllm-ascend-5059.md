---
id: technique-pr-vllm-ascend-5059
title: "PR Insight: vllm-project/vllm-ascend #5059"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - fia
  - mtp
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5059"
---

# PR Insight: vllm-project/vllm-ascend #5059

**Title:** [BugFix]Fix FIA input err in DSv3.1

## Overview
This PR fixes a bug in FIA (Flash Attention) operations when using MTP (Multi-Token Prediction) with full decode only and async scheduling together. The issue was caused by non-increasing 'actual_seq_lengths' input due to incorrect filling of the 'query_start_loc' variable with '-1' instead of 'cu_num_tokens'.

## Technical Significance
The fix ensures correct sequence length tracking for FIA operations in DeepSeek v3.1 models during decode-only scenarios. This is critical for maintaining proper attention computation and memory layout consistency when using Ascend NPUs for MTP inference workloads.

## Related
- technique-flash-attention
- technique-mtp
- kernel-attention-ascendc