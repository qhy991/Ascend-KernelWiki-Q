---
id: technique-pr-modellink-3288
title: "PR Insight: Ascend/ModelLink #3288"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - attention
  - distributed
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3288"
---

# PR Insight: Ascend/ModelLink #3288

**Title:** [pytorch][bugfix]optimize attention mask memory in tuning and dpo.

## Overview
This PR from Ascend/ModelLink addresses: **[pytorch][bugfix]optimize attention mask memory in tuning and dpo.**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed_llm/tasks/checkpoint/convert_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Modellink is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
