---
id: technique-pr-mindspeed-2754
title: "PR Insight: Ascend/MindSpeed #2754"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - distributed
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2754"
---

# PR Insight: Ascend/MindSpeed #2754

**Title:** [bugfix] fixes for fsdp2

## Overview
This PR from Ascend/MindSpeed addresses: **[bugfix] fixes for fsdp2**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed/core/distributed/layerzero/zero3/_common_utils.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
