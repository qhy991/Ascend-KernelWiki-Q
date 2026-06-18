---
id: technique-pr-modellink-2325
title: "PR Insight: Ascend/ModelLink #2325"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen25
  - lora
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2325"
---

# PR Insight: Ascend/ModelLink #2325

**Title:** 添加Qwen2.5 0.5B/1.5B/3B LoRA微调,权重合并及chat脚本 Qwen2.5其他微调脚本添加padded-samples参数

## Overview
This PR adds LoRA fine-tuning scripts, weight merging scripts, and chat inference scripts for Qwen2.5 models (0.5B/1.5B/3B). It also adds `padded-samples` parameter to other Qwen2.5 fine-tuning scripts for handling variable sequence lengths.

## Technical Significance
LoRA fine-tuning reduces memory requirements by freezing base model weights and training only small adapter matrices. The scripts enable efficient parameter-efficient fine-tuning on Ascend NPUs. Weight merging combines adapters with base weights for deployment without runtime overhead. The `padded-samples` parameter optimizes training efficiency by controlling padding behavior for variable-length sequences, improving NPU utilization.

## Related
- `technique-lora-finetuning`
- `technique-weight-merging`
- `technique-padding-optimization`