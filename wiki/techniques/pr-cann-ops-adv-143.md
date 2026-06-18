---
id: technique-pr-cann-ops-adv-143
title: "PR Insight: cann-ops-adv #143"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/143"
---

# PR Insight: cann-ops-adv #143 - 新增MoeInitRoutingV2Grad算子

## Overview
This PR adds the MoeInitRoutingV2Grad operator, which computes gradients for version 2 of the MoE routing initialization during backpropagation, enabling MoE model training.

## Technical Significance
Gradients through routing initialization are essential for training MoE models to learn good expert assignment patterns. This operator enables gradient flow through the routing decision process on Ascend NPUs, supporting end-to-end MoE training.

## Related
- `kernel-moe`
- `kernel-topk`
- `kernel-softmax`
- `hw-vector-unit`