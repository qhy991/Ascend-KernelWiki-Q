---
id: technique-pr-vllm-ascend-95
title: "PR Insight: vllm-project/vllm-ascend #95"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/95"
---

# PR Insight: vllm-project/vllm-ascend #95

**Title:** [BugFix] Add value.contiguous in attention to avoid some accuracy problems.

## Overview
This PR fixes an accuracy issue in attention by adding a value.contiguous() call before attention computation. The fix is minimal (2 lines added to attention.py).

## Technical Significance
Non-contiguous tensors can cause correctness issues in attention kernels, especially when the memory layout doesn't match expected strides. This is a common pitfall in transformer implementations where tensor views are created. The fix ensures proper memory layout before kernel execution.

## Related
- kernel-attention