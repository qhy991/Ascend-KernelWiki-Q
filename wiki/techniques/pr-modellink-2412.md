---
id: technique-pr-modellink-2412
title: "PR Insight: Ascend/ModelLink #2412"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - deepseek
  - lora
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2412"
---

# PR Insight: Ascend/ModelLink #2412

**Title:** fix merge lora ckpt of deepseekV3

## Overview
This PR fixes an issue with merging LoRA checkpoints for DeepSeekV3 models, ensuring that LoRA adapters are correctly combined with base model weights.

## Technical Significance
Proper LoRA checkpoint merging is essential for deploying fine-tuned models; this fix ensures that DeepSeekV3 LoRA adapters are correctly integrated without numerical errors or architectural mismatches.

## Related
- `technique-lora` / `technique-deepseek` / `technique-checkpoint-merging`