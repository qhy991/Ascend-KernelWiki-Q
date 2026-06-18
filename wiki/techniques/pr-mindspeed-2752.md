---
id: technique-pr-mindspeed-2752
title: "PR Insight: Ascend/MindSpeed #2752"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - distributed
  - bugfix
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2752"
---

# PR Insight: Ascend/MindSpeed #2752

**Title:** 【bugfix!!!】fb recompute fix&amp;amp;mtp recompute supported

## Overview
This PR from Ascend/MindSpeed addresses: **【bugfix!!!】fb recompute fix&amp;amp;mtp recompute supported**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/swap_attention/test_swap_attention.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
