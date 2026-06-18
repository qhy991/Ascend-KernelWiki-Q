---
id: technique-pr-mindspeed-2770
title: "PR Insight: Ascend/MindSpeed #2770"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - performance
  - general
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2770"
---

# PR Insight: Ascend/MindSpeed #2770

**Title:** [refactor] optimize tnd in fa

## Overview
This PR from Ascend/MindSpeed addresses: **[refactor] optimize tnd in fa**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/conftest.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
