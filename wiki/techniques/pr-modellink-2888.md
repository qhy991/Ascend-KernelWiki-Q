---
id: technique-pr-modellink-2888
title: "PR Insight: Ascend/ModelLink #2888"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - performance
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2888"
---

# PR Insight: Ascend/ModelLink #2888

**Title:** [pytorch][bugfix]update lora_finetune

## Overview
This PR from Ascend/ModelLink addresses: **[pytorch][bugfix]update lora_finetune**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed_llm/tasks/checkpoint/convert_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Modellink is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
