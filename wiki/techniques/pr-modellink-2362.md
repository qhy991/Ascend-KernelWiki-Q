---
id: technique-pr-modellink-2362
title: "PR Insight: Ascend/ModelLink #2362"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseek3
  - lora
  - weight-conversion
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2362"
---

# PR Insight: Ascend/ModelLink #2362

**Title:** deepseek3 权重转换 lora 合并

## Overview
This PR implements LoRA weight merging during the weight conversion process for DeepSeekV3. The feature enables direct conversion of LoRA-finetuned models from training checkpoints to deployment format with combined weights.

## Technical Significance
Combining LoRA merging with weight conversion streamlines the deployment pipeline for fine-tuned models. For DeepSeekV3, this must correctly handle the MLA compressed representations and MoE expert weights. The integration ensures that LoRA adapters are properly merged with base weights during format conversion, supporting efficient deployment on Ascend inference systems.

## Related
- `technique-lora-finetuning`
- `technique-weight-conversion`
- `kernel-attention-mla`