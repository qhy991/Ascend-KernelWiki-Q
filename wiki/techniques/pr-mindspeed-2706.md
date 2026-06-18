---
id: technique-pr-mindspeed-2706
title: "PR Insight: Ascend/MindSpeed #2706"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - distributed
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2706"
---

# PR Insight: Ascend/MindSpeed #2706

**Title:** use p2p ops instead of batch p2p for PP on NPU for better performance

## Overview
This PR from Ascend/MindSpeed addresses: **use p2p ops instead of batch p2p for PP on NPU for better performance**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `tests_extend/system_tests/feature_precision_guarding/llama_param_cvt.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
