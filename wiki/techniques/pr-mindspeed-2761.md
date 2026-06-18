---
id: technique-pr-mindspeed-2761
title: "PR Insight: Ascend/MindSpeed #2761"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - mindspore
  - general
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2761"
---

# PR Insight: Ascend/MindSpeed #2761

**Title:** [mindspore][patch][master]add patches for third_party

## Overview
This PR from Ascend/MindSpeed addresses: **[mindspore][patch][master]add patches for third_party**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed/mindspore/core/data_parallel/async_log_allreduce.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
