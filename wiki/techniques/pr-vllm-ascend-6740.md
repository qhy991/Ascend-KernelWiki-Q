---
id: technique-pr-vllm-ascend-6740
title: "PR Insight: vllm-project/vllm-ascend #6740"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fused-qkvzba-split-reshape
  - triton
  - qwen3-next
  - kernel-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6740"
---

# PR Insight: vllm-project/vllm-ascend #6740

**Title:** [Feat]fused_qkvzba_split_reshape supports token number greater than 65536

## Overview
This PR optimizes the fused_qkvzba_split_reshape Triton kernel for Qwen3-Next GatedDeltaNet model, refactoring to a loop-based approach that supports arbitrary num_v_heads/num_k_heads ratios and batch sizes. It removes conditional restrictions and fallback paths.

## Technical Significance
Enables Qwen3-Next inference with token counts exceeding 65536 by removing kernel limitations. The optimized implementation provides better memory utilization through configurable ROWS_PER_ITER and handles all scenarios without fallback paths.

## Related
- `kernel-attention`