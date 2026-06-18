---
id: technique-pr-mindspeed-2718
title: "PR Insight: Ascend/MindSpeed #2718"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - gradient
  - general
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2718"
---

# PR Insight: Ascend/MindSpeed #2718

**Title:** verl recompute adaptor

## Overview
This PR from Ascend/MindSpeed addresses: **verl recompute adaptor**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/reuse_fp32_param/test_reuse_fp32_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
