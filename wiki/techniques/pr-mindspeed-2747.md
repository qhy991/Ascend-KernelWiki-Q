---
id: technique-pr-mindspeed-2747
title: "PR Insight: Ascend/MindSpeed #2747"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - kernel
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2747"
---

# PR Insight: Ascend/MindSpeed #2747

**Title:** fix norm patch bug

## Overview
This PR from Ascend/MindSpeed addresses: **fix norm patch bug**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/tensor_parallel/test_layernorm2d.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
