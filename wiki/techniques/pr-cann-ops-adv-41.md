---
id: technique-pr-cann-ops-adv-41
title: "PR Insight: cann-ops-adv #41"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - flash-attention
  - attention
  - performance
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/41"
---

# PR Insight: cann-ops-adv #41 - Update FlashAttentionScore & FlashAttentionScoreGrad, optimize performance

## Overview
This PR updates the FlashAttentionScore and FlashAttentionScoreGrad operators with performance optimizations. These operators implement efficient attention computation and gradients for transformer models on Ascend NPUs.

## Technical Significance
Performance optimizations for attention operators directly impact LLM inference and training throughput. The optimizations likely include improved memory access patterns, better tiling strategies, or more efficient use of Ascend's Cube and Vector units, reducing kernel execution time and increasing hardware utilization.

## Related
- `kernel-flash-attention`
- `kernel-attention`
- `hw-cube-unit`
- `technique-online-softmax`