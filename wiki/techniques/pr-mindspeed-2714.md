---
id: technique-pr-mindspeed-2714
title: "PR Insight: Ascend/MindSpeed #2714"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - distributed
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2714"
---

# PR Insight: Ascend/MindSpeed #2714

**Title:** ulysses cp st fix

## Overview
This PR from Ascend/MindSpeed addresses: **ulysses cp st fix**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/mindspeed/core/context_parallel/test_ringattn_context_parallel_tnd.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
