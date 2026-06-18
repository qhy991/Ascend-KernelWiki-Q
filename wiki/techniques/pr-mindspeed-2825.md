---
id: technique-pr-mindspeed-2825
title: "PR Insight: Ascend/MindSpeed #2825"
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
  - "https://gitee.com/ascend/MindSpeed/pulls/2825"
---

# PR Insight: Ascend/MindSpeed #2825

**Title:** perf: fused moe permute

## Overview
This PR from Ascend/MindSpeed addresses: **perf: fused moe permute**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/moe/test_1f1b_overlap.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
