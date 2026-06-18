---
id: technique-pr-mindspeed-2737
title: "PR Insight: Ascend/MindSpeed #2737"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2737"
---

# PR Insight: Ascend/MindSpeed #2737

**Title:** fix: dist ckpt save

## Overview
This PR from Ascend/MindSpeed addresses: **fix: dist ckpt save**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/conftest.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
