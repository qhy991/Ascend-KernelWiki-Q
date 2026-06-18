---
id: technique-pr-modellink-2368
title: "PR Insight: Ascend/ModelLink #2368"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - lora
  - bugfix
  - checkpoint-merging
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2368"
---

# PR Insight: Ascend/ModelLink #2368

**Title:** fix lora_path is None when merge lora_ckpt

## Overview
This PR fixes a bug where `lora_path` becomes None when merging LoRA (Low-Rank Adaptation) checkpoints. The issue prevented proper weight combination between base model weights and LoRA adapter weights.

## Technical Significance
LoRA fine-tuning is a parameter-efficient method that adds small adapter matrices to pre-trained models. Merging LoRA checkpoints with base models requires precise weight aggregation. This bug fix ensures that the LoRA adapter path is correctly resolved during checkpoint merging, enabling deployment of LoRA-finetuned models on Ascend hardware without requiring the separate adapter files during inference.

## Related
- `technique-lora-finetuning`
- `technique-weight-merging`