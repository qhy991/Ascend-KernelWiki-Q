---
id: technique-pr-modellink-2808
title: "PR Insight: Ascend/ModelLink #2808"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mindspore
  - qwen
  - finetune
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2808"
---

# PR Insight: Ascend/ModelLink #2808

**Title:** adapte qwen25_32b_ms tune and generate

## Overview
This PR adapts Qwen2.5 32B model for fine-tuning and generation in the MindSpore backend. It adds configurations and scripts for these workflows.

## Technical Significance
Enabling fine-tuning and generation for Qwen2.5 32B expands the model's utility on Ascend NPUs. This support allows users to adapt and deploy this mid-sized model for various applications using MindSpore.

## Related
- `technique-distributed-training`