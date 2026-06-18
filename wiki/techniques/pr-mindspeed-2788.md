---
id: technique-pr-mindspeed-2788
title: "PR Insight: Ascend/MindSpeed #2788"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - general
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2788"
---

# PR Insight: Ascend/MindSpeed #2788

**Title:** feat: verl noop layer adaptor

## Overview
This PR from Ascend/MindSpeed addresses: **feat: verl noop layer adaptor**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/reuse_fp32_param/test_reuse_fp32_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
