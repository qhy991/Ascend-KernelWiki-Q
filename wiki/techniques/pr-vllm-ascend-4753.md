---
id: technique-pr-vllm-ascend-4753
title: "PR Insight: vllm-project/vllm-ascend #4753"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseekv3
  - mla
  - mlapo
  - attention
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4753"
---

# PR Insight: vllm-project/vllm-ascend #4753

**Title:** Support DeepSeekV3.2 with MLAPO operator

## Overview
This PR adds support for the optimized MLAPO operator in DeepSeekV3.2. The operator provides an optimized implementation that avoids redundant q_down recomputation, improving computational efficiency. This integrates the MLAPO operator implementation introduced in PR #4707.

## Technical Significance
Enables the use of the MLAPO (Multi-Linear Attention with Projection Optimization) operator for DeepSeekV3.2 models, avoiding redundant q_down projections during attention computation. This optimization reduces redundant computation in the MLA attention mechanism.

## Related
- `kernel-mlapo`
- `technique-mla`
- `kernel-deepseekv3`
- `technique-attention-optimization`