---
id: technique-pr-mindspeed-2748
title: "PR Insight: Ascend/MindSpeed #2748"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - distributed
  - bugfix
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2748"
---

# PR Insight: Ascend/MindSpeed #2748

**Title:** fix ddp overlap-param-gather issue when param order and forward mismatch

## Overview
This PR from Ascend/MindSpeed addresses: **fix ddp overlap-param-gather issue when param order and forward mismatch**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/reuse_fp32_param/test_reuse_fp32_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
