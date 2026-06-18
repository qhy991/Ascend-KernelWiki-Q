---
id: technique-pr-modellink-2410
title: "PR Insight: Ascend/ModelLink #2410"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - moe
  - qwen
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2410"
---

# PR Insight: Ascend/ModelLink #2410

**Title:** 严重单：Qwen2_MOE 前向精度问题

## Overview
This PR fixes a forward pass precision issue in Qwen2-MoE models, ensuring numerical correctness during inference and training forward propagation.

## Technical Significance
Precision issues in MoE models can significantly affect output quality and downstream task performance; this fix ensures that Qwen2-MoE models produce accurate results on Ascend hardware.

## Related
- `technique-moe` / `technique-precision` / `technique-qwen` / `technique-numerical-stability`