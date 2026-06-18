---
id: technique-pr-mindspeed-2778
title: "PR Insight: Ascend/MindSpeed #2778"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - bugfix
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2778"
---

# PR Insight: Ascend/MindSpeed #2778

**Title:** fix: MoEAlltoAllSeqOverLapDispatcher and moe_permute_fusion

## Overview
This PR from Ascend/MindSpeed addresses: **fix: MoEAlltoAllSeqOverLapDispatcher and moe_permute_fusion**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed/mindspore/core/transformer/moe/moe_feature/tp_extend_ep/token_dispatcher.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
