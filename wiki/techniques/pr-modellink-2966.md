---
id: technique-pr-modellink-2966
title: "PR Insight: Ascend/ModelLink #2966"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - distributed
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2966"
---

# PR Insight: Ascend/ModelLink #2966

**Title:** [pytorch][bugfix]fix vpp of V3_ckpt

## Overview
This PR from Ascend/ModelLink addresses: **[pytorch][bugfix]fix vpp of V3_ckpt**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed_llm/tasks/checkpoint/convert_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Modellink is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
