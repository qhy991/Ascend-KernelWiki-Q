---
id: technique-pr-mindspeed-2784
title: "PR Insight: Ascend/MindSpeed #2784"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2784"
---

# PR Insight: Ascend/MindSpeed #2784

**Title:** perf: moe permute fusion

## Overview
This PR from Ascend/MindSpeed addresses: **perf: moe permute fusion**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/moe/test_1f1b_overlap.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
