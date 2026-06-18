---
id: technique-pr-mindspeed-2814
title: "PR Insight: Ascend/MindSpeed #2814"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - performance
  - memory-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2814"
---

# PR Insight: Ascend/MindSpeed #2814

**Title:** docs: swap and virtual optimizer

## Overview
This PR from Ascend/MindSpeed addresses: **docs: swap and virtual optimizer**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/tools/data_handler.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
