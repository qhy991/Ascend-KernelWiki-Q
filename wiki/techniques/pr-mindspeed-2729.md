---
id: technique-pr-mindspeed-2729
title: "PR Insight: Ascend/MindSpeed #2729"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - distributed
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2729"
---

# PR Insight: Ascend/MindSpeed #2729

**Title:** [bugfix!!!]shared_expert_gate remove&amp;amp; logits adjust &amp;amp; overlap readme append

## Overview
This PR from Ascend/MindSpeed addresses: **[bugfix!!!]shared_expert_gate remove&amp;amp; logits adjust &amp;amp; overlap readme append**. It is part of the Ascend training framework's ongoing development for large-model distributed training on NPU hardware.
  - `mindspeed/mindspore/core/transformer/moe/moe_layer_overlap_all2all.py`

## Technical Significance
The change impacts Ascend NPU training performance and/or correctness in the context of large-scale distributed model training. Mindspeed is a training acceleration framework that works with Megatron/MindSpore/PyTorch backends, and this PR contributes to its stability, performance, or feature coverage on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`
