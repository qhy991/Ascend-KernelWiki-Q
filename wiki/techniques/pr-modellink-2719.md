---
id: technique-pr-modellink-2719
title: "PR Insight: Ascend/ModelLink #2719"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - lora
  - qwen3
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2719"
---

# PR Insight: Ascend/ModelLink #2719

**Title:** fix script of lora-sft of qwen3

## Overview
This PR fixes issues in the LoRA-SFT (Supervised Fine-Tuning) scripts for Qwen3 models. The fix resolves problems that prevented proper fine-tuning using the LoRA method on Qwen3 models.

## Technical Significance
LoRA-SFT is a popular method for efficient model adaptation. Fixing these scripts ensures that Qwen3 models can be fine-tuned efficiently on Ascend NPUs using LoRA, enabling parameter-efficient adaptation with minimal additional computational resources.

## Related
- technique-operator-fusion