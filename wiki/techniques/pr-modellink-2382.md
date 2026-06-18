---
id: technique-pr-modellink-2382
title: "PR Insight: Ascend/ModelLink #2382"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2382"
---

# PR Insight: Ascend/ModelLink #2382

**Title:** 新增Qwen2-MoE非Pack场景全参微调脚本

## Overview
This PR adds full-parameter fine-tuning scripts for Qwen2-MoE models in non-packed scenarios, enabling comprehensive fine-tuning of MoE models without using packing optimizations.

## Technical Significance
Non-packed fine-tuning scenarios provide flexibility for training MoE models where packing optimizations may not be applicable or desired, ensuring full control over training dynamics and expert routing.

## Related
- `technique-moe` / `technique-fine-tuning` / `technique-qwen` / `technique-full-parameter`