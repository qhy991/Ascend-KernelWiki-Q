---
id: technique-pr-mindspeed-2733
title: "PR Insight: Ascend/MindSpeed #2733"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - training
  - general
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2733"
---

# PR Insight: Ascend/MindSpeed #2733

**Title:** add resume training ST for dist ckpt and torch ckpt

## Overview
This PR from Ascend/MindSpeed addresses: **add resume training ST for dist ckpt and torch ckpt**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed/core/distributed/layerzero/state/mga_checkpoint.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
