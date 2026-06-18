---
id: technique-pr-vllm-ascend-5390
title: "PR Insight: vllm-project/vllm-ascend #5390"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mla
  - attention
  - transpose-elimination
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5390"
---

# PR Insight: vllm-project/vllm-ascend #5390

**Title:** [Feature] Remove the transpose step after attention and switch to transpose_batchmatmul

## Overview
This PR optimizes MLA by eliminating the transpose operation after attention and switching to `transpose_batchmatmul`. The `npu_fused_infer_attention_score` kernel now supports specifying output layout to avoid unnecessary transposes, and `transpose_batchmatmul` controls output tensor transposition via `perm_y`.

## Technical Significance
Eliminating unnecessary transpose operations reduces memory bandwidth usage and improves MLA performance. The optimization leverages Ascend NPU's flexible attention and matrix multiplication kernels to produce data in the optimal layout directly.

## Related
- technique-mla
- technique-attention
- technique-transpose-elimination