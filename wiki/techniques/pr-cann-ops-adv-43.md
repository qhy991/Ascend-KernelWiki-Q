---
id: technique-pr-cann-ops-adv-43
title: "PR Insight: cann-ops-adv #43"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/43"
---

# PR Insight: cann-ops-adv #43 - Update PFA & IFA & FIA, optimize performance

## Overview
This PR updates three attention operators—PFA (PromptFlashAttention), IFA (IncreFlashAttention), and FIA (FusedInferAttentionScore)—with performance optimizations for different transformer inference scenarios.

## Technical Significance
Optimizing all three attention operators comprehensively improves LLM inference across different phases: prompt processing (PFA), incremental generation (IFA), and fused inference (FIA). Performance improvements likely involve better memory management, optimized tiling, or improved hardware utilization across Ascend's compute units.

## Related
- `kernel-flash-attention`
- `kernel-attention`
- `technique-operator-fusion`
- `hw-cube-unit`