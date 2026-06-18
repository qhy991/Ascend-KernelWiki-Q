---
id: technique-pr-vllm-ascend-1896
title: "PR Insight: vllm-project/vllm-ascend #1896"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek
  - eplb
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1896"
---

# PR Insight: vllm-project/vllm-ascend #1896

**Title:** [0.9.1][bugfix] fix static eplb

## Overview
This PR fixes a bug when running DeepSeek models with static EPLB (Expert Per-Token Load Balancing). The fix ensures proper EPLB functionality in static configuration mode.

## Technical Significance
Bugfix for EPLB feature. EPLB is critical for load balancing in MoE models, and incorrect behavior in static mode could lead to expert imbalance and performance degradation.

## Related
- `technique-moe`
- `technique-eplb`
- `technique-deepseek`