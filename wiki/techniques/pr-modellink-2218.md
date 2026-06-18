---
id: technique-pr-modellink-2218
title: "PR Insight: Ascend/ModelLink #2218"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - training
  - qwen
  - sft
  - lora
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2218"
---

# PR Insight: Ascend/ModelLink #2218

**Title:** qwen2.5 sft/lora微调上库

## Overview
Adds support for Qwen2.5 supervised fine-tuning (SFT) and LoRA fine-tuning. This enables users to fine-tune Qwen2.5 models using both full parameter fine-tuning and parameter-efficient LoRA methods.

## Technical Significance
Expands modellink's training capabilities to support the latest Qwen2.5 model with both SFT and LoRA fine-tuning approaches. This provides flexibility for different resource constraints and training scenarios on Ascend hardware.

## Related
- technique-hccl-optimization