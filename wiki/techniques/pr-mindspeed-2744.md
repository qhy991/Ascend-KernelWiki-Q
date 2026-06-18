---
id: technique-pr-mindspeed-2744
title: "PR Insight: Ascend/MindSpeed #2744"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - general
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2744"
---

# PR Insight: Ascend/MindSpeed #2744

**Title:** fix: fix the non-standard html table

## Overview
This PR from Ascend/MindSpeed addresses: **fix: fix the non-standard html table**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/mindspeed/core/context_parallel/test_mapping.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
