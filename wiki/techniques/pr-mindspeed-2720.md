---
id: technique-pr-mindspeed-2720
title: "PR Insight: Ascend/MindSpeed #2720"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - mindspore
  - distributed
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2720"
---

# PR Insight: Ascend/MindSpeed #2720

**Title:** [mindspore][bugfix][master] fix pp schedule shape error

## Overview
This PR from Ascend/MindSpeed addresses: **[mindspore][bugfix][master] fix pp schedule shape error**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed/mindspore/core/data_parallel/async_log_allreduce.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
