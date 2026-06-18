---
id: technique-pr-modellink-2837
title: "PR Insight: Ascend/ModelLink #2837"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - lora
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2837"
---

# PR Insight: Ascend/ModelLink #2837

**Title:** [pytorch][bugfix]update qwen25-72b-4k-lora

## Overview
This PR fixes issues with the Qwen2.5 72B 4K LoRA fine-tuning configuration in the PyTorch backend. It updates scripts and configurations to ensure proper LoRA fine-tuning execution.

## Technical Significance
LoRA fine-tuning is a memory-efficient technique for adapting large models. Fixing these issues ensures users can successfully fine-tune Qwen2.5 72B on Ascend NPUs with reduced memory footprint, making large model adaptation more accessible.

## Related
- `technique-distributed-training`