---
id: technique-pr-modellink-3371
title: "PR Insight: Ascend/ModelLink #3371"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - bugfix
  - kernel
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3371"
---

# PR Insight: Ascend/ModelLink #3371

**Title:** [pytorch][bugfix]restore the einsum operation for next states of mamba

## Overview
This PR from Ascend/ModelLink addresses: **[pytorch][bugfix]restore the einsum operation for next states of mamba**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed_llm/tasks/checkpoint/convert_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Modellink is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
