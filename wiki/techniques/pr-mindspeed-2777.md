---
id: technique-pr-mindspeed-2777
title: "PR Insight: Ascend/MindSpeed #2777"
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
  - "https://gitee.com/ascend/MindSpeed/pulls/2777"
---

# PR Insight: Ascend/MindSpeed #2777

**Title:** [Bugfix] 修复 dist_train

## Overview
This PR from Ascend/MindSpeed addresses: **[Bugfix] 修复 dist_train**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/multi_model/dist_train/test_dist_schedules.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
