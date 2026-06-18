---
id: technique-pr-modellink-2983
title: "PR Insight: Ascend/ModelLink #2983"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2983"
---

# PR Insight: Ascend/ModelLink #2983

**Title:** [pytorch][sh]update llama2-70b 128k poc script

## Overview
This PR from Ascend/ModelLink addresses: **[pytorch][sh]update llama2-70b 128k poc script**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed_llm/tasks/checkpoint/convert_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Modellink is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
