---
id: technique-pr-vllm-ascend-10117
title: "PR Insight: vllm-project/vllm-ascend #10117"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - data-parallel
  - hanging
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10117"
---

# PR Insight: vllm-project/vllm-ascend #10117

**Title:** [main][BugFix] Avoid the issue of moe hanging in multi-DP scenarios without introducing new problems

## Overview
This PR fixes MoE hanging issues in multi-data-parallel scenarios without introducing new problems. It addresses deadlock or hanging conditions that occurred during MoE execution with multiple data parallel ranks.

## Technical Significance
Resolves MoE hanging in multi-DP scenarios by fixing communication or synchronization issues. Ensures that MoE models run reliably with data parallelism without introducing new bugs, improving system stability for distributed MoE inference.

## Related
- `technique-moe`, `technique-data-parallel`, `technique-hccl-optimization`, `pattern-deadlock-prevention`