---
id: technique-pr-mindspeed-2750
title: "PR Insight: Ascend/MindSpeed #2750"
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
  - "https://gitee.com/ascend/MindSpeed/pulls/2750"
---

# PR Insight: Ascend/MindSpeed #2750

**Title:** fix: layer norm error

## Overview
This PR from Ascend/MindSpeed addresses: **fix: layer norm error**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/features/unaligned_linear/test_unaligned_linear.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
