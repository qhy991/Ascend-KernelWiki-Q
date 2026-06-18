---
id: technique-pr-modellink-2735
title: "PR Insight: Ascend/ModelLink #2735"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - lora
  - qwen3
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2735"
---

# PR Insight: Ascend/ModelLink #2735

**Title:** add lora-sft and fix scripts of qwen3

## Overview
This PR adds LoRA-SFT (Supervised Fine-Tuning) support for ModelLink and fixes scripts related to Qwen3 models. The additions enable efficient parameter-efficient fine-tuning using LoRA.

## Technical Significance
LoRA-SFT is a cost-effective method for adapting models to specific tasks. This support enables efficient fine-tuning of various models on Ascend NPUs with minimal additional compute and memory overhead, while also fixing issues with Qwen3 scripts.

## Related
- technique-operator-fusion