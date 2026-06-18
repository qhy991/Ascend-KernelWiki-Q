---
id: technique-pr-mindspeed-2757
title: "PR Insight: Ascend/MindSpeed #2757"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - general
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2757"
---

# PR Insight: Ascend/MindSpeed #2757

**Title:** adjust hash implementation

## Overview
This PR from Ascend/MindSpeed addresses: **adjust hash implementation**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed/core/memory/adaptive_memory/adaptive_memory_swap_manager.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
