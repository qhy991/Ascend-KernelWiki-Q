---
id: technique-pr-modellink-2733
title: "PR Insight: Ascend/ModelLink #2733"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - glm4
  - training
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2733"
---

# PR Insight: Ascend/ModelLink #2733

**Title:** add glm4-9b 预训练、微调、推理、评测、权重转换、数据处理

## Overview
This PR adds complete support for the GLM4 9B model, including pretraining, fine-tuning, inference, evaluation, weight conversion, and data processing scripts. It provides comprehensive workflows for training and deploying this model on Ascend hardware.

## Technical Significance
GLM4 is an important open-source Chinese language model. Adding full support enables researchers and developers to leverage Ascend NPUs for efficient training and deployment of GLM4 9B across all stages of the machine learning pipeline.

## Related
- technique-operator-fusion