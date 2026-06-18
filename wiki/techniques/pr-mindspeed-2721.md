---
id: technique-pr-mindspeed-2721
title: "PR Insight: Ascend/MindSpeed #2721"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - attention
  - distributed
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2721"
---

# PR Insight: Ascend/MindSpeed #2721

**Title:** fix: 修复tp2d不开cp时走ring attn

## Overview
This PR from Ascend/MindSpeed addresses: **fix: 修复tp2d不开cp时走ring attn**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/multi_model/dist_train/test_dist_schedules.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
