---
id: technique-pr-vllm-ascend-2758
title: "PR Insight: vllm-project/vllm-ascend #2758"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - attention
  - sliding-window
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2758"
---

# PR Insight: vllm-project/vllm-ascend #2758

**Title:** [fix] prefill unsupport sliding window attention

## Overview
This PR fixes a prefill phase attention bug where sliding window attention was incorrectly supported. The `npu_fused_infer_attention_score` operator only supports head_dim of 128 and cannot handle other dimensions required by sliding window attention.

## Technical Significance
Correct attention operator selection is essential for accuracy and performance. Removing unsupported sliding window support in prefill phase prevents runtime errors and ensures proper fallback to alternative attention implementations on Ascend NPU.

## Related
- `kernel-attention`
- `technique-sliding-window`
- `kernel-npu-fused-attention`
- `technique-attention-selection`