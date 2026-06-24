---
id: technique-pr-mindspeed-2796
title: 'PR Insight: Ascend/MindSpeed #2796'
type: wiki-technique
architectures:
- ascend910
- ascend910b
tags:
- mindspeed
- attention
- distributed
- feature
confidence: inferred
sources:
- pr-mindspeed-2796
---

# PR Insight: Ascend/MindSpeed #2796

**Title:** mla supports ring-attention and tp

## Overview
This PR from Ascend/MindSpeed addresses: **mla supports ring-attention and tp**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/unit_tests/mindspeed/core/context_parallel/test_mapping.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
