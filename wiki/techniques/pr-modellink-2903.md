---
id: technique-pr-modellink-2903
title: "PR Insight: Ascend/ModelLink #2903"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mindspore
  - bugfix
  - memory-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2903"
---

# PR Insight: Ascend/ModelLink #2903

**Title:** 【mindspore】【bugfix】【2.1.0】fix glm4 memory

## Overview
This PR from Ascend/ModelLink addresses: **【mindspore】【bugfix】【2.1.0】fix glm4 memory**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `ci/access_control_test_ms.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Modellink is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
