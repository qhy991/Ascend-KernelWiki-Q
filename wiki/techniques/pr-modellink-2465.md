---
id: technique-pr-modellink-2465
title: "PR Insight: Ascend/ModelLink #2465"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2465"
---

# PR Insight: Ascend/ModelLink #2465

**Title:** deepseekV3 LORA to HF

## Overview
This PR adds LoRA (Low-Rank Adaptation) weight conversion support for DeepSeekV3 models to HuggingFace format. It enables users to convert trained LoRA checkpoints from the ModelLink framework to the standard HF format for downstream deployment and inference.

## Technical Significance
The conversion bridges ModelLink's proprietary training format with the broader HuggingFace ecosystem, allowing DeepSeekV3 LoRA-fine-tuned models to be used across different inference frameworks and tools.

## Related
- `technique-lora` / `technique-weight-conversion`