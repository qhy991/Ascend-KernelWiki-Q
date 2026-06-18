---
id: technique-pr-mindspeed-2728
title: "PR Insight: Ascend/MindSpeed #2728"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - general
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2728"
---

# PR Insight: Ascend/MindSpeed #2728

**Title:** 【bugfix】修复fb ov中drop and pad模式device错误

## Overview
This PR from Ascend/MindSpeed addresses: **【bugfix】修复fb ov中drop and pad模式device错误**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.


## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
