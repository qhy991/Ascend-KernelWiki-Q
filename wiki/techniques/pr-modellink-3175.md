---
id: technique-pr-modellink-3175
title: "PR Insight: Ascend/ModelLink #3175"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - general
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3175"
---

# PR Insight: Ascend/ModelLink #3175

**Title:** [pytorch][sh] qwen3-30b script update

## Overview
This PR from Ascend/ModelLink addresses: **[pytorch][sh] qwen3-30b script update**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed_llm/tasks/checkpoint/convert_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Modellink is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
