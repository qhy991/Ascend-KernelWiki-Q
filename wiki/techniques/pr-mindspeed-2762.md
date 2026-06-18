---
id: technique-pr-mindspeed-2762
title: "PR Insight: Ascend/MindSpeed #2762"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - mindspore
  - distributed
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2762"
---

# PR Insight: Ascend/MindSpeed #2762

**Title:** [feature][mindspore] support qwenvl-25-lora using Tensor.backward

## Overview
This PR from Ascend/MindSpeed addresses: **[feature][mindspore] support qwenvl-25-lora using Tensor.backward**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/reuse_fp32_param/test_reuse_fp32_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
