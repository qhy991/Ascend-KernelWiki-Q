---
id: technique-pr-mindspeed-2715
title: "PR Insight: Ascend/MindSpeed #2715"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - kernel
  - general
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2715"
---

# PR Insight: Ascend/MindSpeed #2715

**Title:** adjust LayerNorm patch

## Overview
This PR from Ascend/MindSpeed addresses: **adjust LayerNorm patch**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed/core/memory/adaptive_memory/adaptive_memory_swap_manager.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
