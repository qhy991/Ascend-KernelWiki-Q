---
id: technique-pr-modellink-3023
title: "PR Insight: Ascend/ModelLink #3023"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3023"
---

# PR Insight: Ascend/ModelLink #3023

**Title:** [pytorch][md]update docs for pretrain and finetuning

## Overview
This PR from Ascend/ModelLink addresses: **[pytorch][md]update docs for pretrain and finetuning**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed_llm/tasks/checkpoint/convert_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Modellink is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
