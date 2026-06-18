---
id: technique-pr-modellink-2771
title: "PR Insight: Ascend/ModelLink #2771"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen
  - training
  - distillation
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2771"
---

# PR Insight: Ascend/ModelLink #2771

**Title:** 【feature】【master】Add Deepseek R1 distillation of Qwen2.5 math 7B model…

## Overview
This PR adds scripts and configuration for distilling the DeepSeek R1 model into Qwen2.5 math 7B model. Knowledge distillation transfers capabilities from a larger teacher model (DeepSeek R1) to a smaller student model (Qwen2.5).

## Technical Significance
DeepSeek R1 distillation is important for creating efficient mathematical reasoning models. This enables training smaller, faster models that retain strong math capabilities on Ascend hardware, which is valuable for applications requiring efficient inference.

## Related
- technique-operator-fusion