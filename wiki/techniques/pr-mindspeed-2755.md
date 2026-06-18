---
id: technique-pr-mindspeed-2755
title: "PR Insight: Ascend/MindSpeed #2755"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - performance
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2755"
---

# PR Insight: Ascend/MindSpeed #2755

**Title:** perf: moe_permute_fusion adapts to other moe features

## Overview
This PR from Ascend/MindSpeed addresses: **perf: moe_permute_fusion adapts to other moe features**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/moe/test_1f1b_overlap.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
