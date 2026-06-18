---
id: technique-pr-modellink-2366
title: "PR Insight: Ascend/ModelLink #2366"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseek3
  - lora
  - weight-merging
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2366"
---

# PR Insight: Ascend/ModelLink #2366

**Title:** deepseek3新增lora权重、base权重合并

## Overview
This PR adds support for merging LoRA adapter weights with base model weights for DeepSeekV3. The feature enables deployment of LoRA-finetuned DeepSeekV3 models by combining adapter weights into the base model weights.

## Technical Significance
DeepSeekV3's MLA and MoE architectures require careful weight merging for LoRA adapters. The merge operation must correctly handle the compressed key-value representations and expert routing weights. This feature enables efficient deployment of parameter-efficient fine-tuned DeepSeekV3 models on Ascend NPUs, eliminating the runtime overhead of maintaining separate adapter matrices during inference.

## Related
- `technique-lora-finetuning`
- `kernel-attention-mla`
- `technique-moe-training`