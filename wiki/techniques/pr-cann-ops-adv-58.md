---
id: technique-pr-cann-ops-adv-58
title: "PR Insight: cann-ops-adv #58"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - flash-attention
  - attention
  - tiling-strategy
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/58"
---

# PR Insight: cann-ops-adv #58 - PFA tiling 优化

## Overview
This PR optimizes the tiling strategy for PFA (PromptFlashAttention), improving data partitioning and memory access patterns for efficient prompt processing.

## Technical Significance
Tiling optimization is critical for maximizing Ascend's on-chip Unified Buffer utilization. Improved tiling reduces global memory access, increases data reuse, and better aligns with hardware constraints, leading to higher performance for prompt processing in LLM inference.

## Related
- `kernel-flash-attention`
- `technique-tiling-strategy`
- `hw-unified-buffer`
- `hw-cube-unit`