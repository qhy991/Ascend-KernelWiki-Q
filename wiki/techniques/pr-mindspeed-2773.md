---
id: technique-pr-mindspeed-2773
title: "PR Insight: Ascend/MindSpeed #2773"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - bugfix
  - memory-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2773"
---

# PR Insight: Ascend/MindSpeed #2773

**Title:** fix: drop_and_pad and moe_zero_memory level0; docs: moe_permute_fusion

## Overview
This PR from Ascend/MindSpeed addresses: **fix: drop_and_pad and moe_zero_memory level0; docs: moe_permute_fusion**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed/mindspore/core/transformer/moe/legacy_a2a_token_dispatcher.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
