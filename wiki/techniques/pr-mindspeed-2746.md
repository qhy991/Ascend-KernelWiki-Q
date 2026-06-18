---
id: technique-pr-mindspeed-2746
title: "PR Insight: Ascend/MindSpeed #2746"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - performance
  - feature
  - memory-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2746"
---

# PR Insight: Ascend/MindSpeed #2746

**Title:** feat: verl swap optimizer adaptor

## Overview
This PR from Ascend/MindSpeed addresses: **feat: verl swap optimizer adaptor**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/reuse_fp32_param/test_reuse_fp32_param.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
