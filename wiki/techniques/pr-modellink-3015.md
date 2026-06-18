---
id: technique-pr-modellink-3015
title: "PR Insight: Ascend/ModelLink #3015"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mindspore
  - performance
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/3015"
---

# PR Insight: Ascend/ModelLink #3015

**Title:** [mindspore][bugfix][sh] fix qwen25_7b tune script

## Overview
This PR from Ascend/ModelLink addresses: **[mindspore][bugfix][sh] fix qwen25_7b tune script**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `ci/access_control_test_ms.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Modellink is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
