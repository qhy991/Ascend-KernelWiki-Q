---
id: technique-pr-vllm-ascend-1614
title: "PR Insight: vllm-project/vllm-ascend #1614"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - deepseek
  - rope
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1614"
---

# PR Insight: vllm-project/vllm-ascend #1614

**Title:** [0.9.1][Perf] Optimize the number of rope-related index selections in deepseek

## Overview
This PR optimizes the number of RoPE (rotary position embedding) index selections for DeepSeek models, improving inference performance.

## Technical Significance
Reduces redundant index computations in RoPE for DeepSeek models, decreasing computational overhead during inference. The optimization is particularly beneficial for long sequences where RoPE index operations accumulate.

## Related
- `technique-rotary-embedding`
- `kernel-deepseek`