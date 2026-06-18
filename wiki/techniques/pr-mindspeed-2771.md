---
id: technique-pr-mindspeed-2771
title: "PR Insight: Ascend/MindSpeed #2771"
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
  - "https://gitee.com/ascend/MindSpeed/pulls/2771"
---

# PR Insight: Ascend/MindSpeed #2771

**Title:** fix: adjust inappropriate config

## Overview
This PR from Ascend/MindSpeed addresses: **fix: adjust inappropriate config**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed/core/memory/adaptive_memory/adaptive_memory_swap_manager.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
