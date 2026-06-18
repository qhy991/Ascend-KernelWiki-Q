---
id: technique-pr-modellink-2783
title: "PR Insight: Ascend/ModelLink #2783"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen
  - lora
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2783"
---

# PR Insight: Ascend/ModelLink #2783

**Title:** add lora-ckpt of qwen3

## Overview
This PR adds LoRA checkpoint support for Qwen3 model. It enables saving and loading LoRA fine-tuned model checkpoints.

## Technical Significance
LoRA checkpoint support is essential for efficient model fine-tuning on Ascend NPUs. This feature allows users to save and load adapter weights without storing full model checkpoints, reducing storage requirements.

## Related
- `technique-distributed-training`