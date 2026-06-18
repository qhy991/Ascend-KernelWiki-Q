---
id: technique-pr-vllm-ascend-4944
title: "PR Insight: vllm-project/vllm-ascend #4944"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - dcp
  - vectorization
  - attention-cp
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4944"
---

# PR Insight: vllm-project/vllm-ascend #4944

**Title:** [Perf] vectorize PCP/DCP loops in attention_cp.py

## Overview
This PR optimizes attention_cp.py by (1) adding explicit .contiguous() after permute/view operations to ensure memory-friendly layout, and (2) replacing nested PCP/DCP Python loops with fully vectorized tensor operations.

## Technical Significance
Significantly improves performance of context parallelism in attention by replacing Python loops with vectorized operations and ensuring contiguous memory layout. This reduces overhead in token routing across context parallel ranks.

## Related
- `kernel-attention-cp`
- `technique-context-parallelism`
- `technique-vectorization`
- `kernel-pcp`
- `kernel-dcp`