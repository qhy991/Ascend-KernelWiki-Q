---
id: technique-pr-cann-ops-adv-233
title: "PR Insight: cann-ops-adv #233"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - gradient
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/233"
---

# PR Insight: cann-ops-adv #233 - moe init routing v2 grad

## Overview
This PR adds gradient computation for MoE Init Routing V2, enabling backpropagation through version 2 of the MoE routing initialization for MoE model training on Ascend NPUs.

## Technical Significance
Gradients through routing initialization enable training MoE models to learn good expert assignment patterns. This operator ensures correct gradient flow through the routing decision process on Ascend NPUs, supporting end-to-end MoE model training.

## Related
- `kernel-moe`
- `kernel-topk`
- `kernel-softmax`
- `hw-vector-unit`