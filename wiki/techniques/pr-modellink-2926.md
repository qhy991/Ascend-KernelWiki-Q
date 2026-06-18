---
id: technique-pr-modellink-2926
title: "PR Insight: Ascend/ModelLink #2926"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mindspore
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2926"
---

# PR Insight: Ascend/ModelLink #2926

**Title:** [mindspore][sh] add mindspore shell of qwen3 14b and 32b pretrain

## Overview
This PR from Ascend/ModelLink addresses: **[mindspore][sh] add mindspore shell of qwen3 14b and 32b pretrain**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `ci/access_control_test_ms.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Modellink is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
