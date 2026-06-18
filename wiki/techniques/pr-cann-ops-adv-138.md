---
id: technique-pr-cann-ops-adv-138
title: "PR Insight: cann-ops-adv #138"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - softmax
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/138"
---

# PR Insight: cann-ops-adv #138 - add op MoeGatingTopKSoftmaxV2

## Overview
This PR adds the MoeGatingTopKSoftmaxV2 operator, which computes Top-K expert selection and softmax gating probabilities for MoE routing. This is version 2 of the operator.

## Technical Significance
MoE gating combines Top-K selection with softmax to determine which experts process each token and with what weight. MoeGatingTopKSoftmaxV2 likely improves upon the original with better numerical stability, faster Top-K selection, or support for additional load balancing techniques.

## Related
- `kernel-moe`
- `kernel-topk`
- `kernel-softmax`
- `hw-vector-unit`