---
id: technique-pr-modellink-2454
title: "PR Insight: Ascend/ModelLink #2454"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - lora
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2454"
---

# PR Insight: Ascend/ModelLink #2454

**Title:** 增加llama3.1-8b微调脚本

## Overview
This PR adds fine-tuning scripts for the Llama 3.1-8B model, enabling efficient parameter-efficient training workflows for this specific model size and architecture within the ModelLink framework.

## Technical Significance
Expands ModelLink's model coverage to include Llama 3.1 variants, providing out-of-the-box training configurations for 8B parameter models with proper hardware mapping and optimization settings for Ascend NPUs.

## Related
- `technique-lora` / `technique-fine-tuning`