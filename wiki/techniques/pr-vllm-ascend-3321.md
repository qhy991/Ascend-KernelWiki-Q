---
id: technique-pr-vllm-ascend-3321
title: "PR Insight: vllm-project/vllm-ascend #3321"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3321"
---

# PR Insight: vllm-project/vllm-ascend #3321

**Title:** [Perf] Add FIA interface in FA case

## Overview
Add new npu_fused_infer_attention_score op to improve perfomance in flash attention case.

## Technical Significance
Adds Fused Infer Attention (FIA) interface support for optimized attention computation in flash attention scenarios.

## Related
- `hw-cube-unit`
