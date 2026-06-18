---
id: technique-pr-cann-ops-adv-155
title: "PR Insight: cann-ops-adv #155"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/155"
---

# PR Insight: cann-ops-adv #155 - 1、新增MoeGatingTopKSoftmax

## Overview
This PR adds the MoeGatingTopKSoftmax operator, which computes Top-K expert selection and softmax gating probabilities for MoE routing, determining which experts process each token.

## Technical Significance
MoE gating combines Top-K selection with softmax to determine expert assignment and weighting. This operator is essential for load balancing in MoE models and enables efficient expert selection on Ascend NPUs with optimized memory access patterns.

## Related
- `kernel-moe`
- `kernel-topk`
- `kernel-softmax`
- `hw-vector-unit`