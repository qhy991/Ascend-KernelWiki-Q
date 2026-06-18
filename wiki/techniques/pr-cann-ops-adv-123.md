---
id: technique-pr-cann-ops-adv-123
title: "PR Insight: cann-ops-adv #123"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - ascendc
  - topk
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/123"
---

# PR Insight: cann-ops-adv #123 - 新增MoeInitRoutingV2算子

## Overview
This PR adds the MoeInitRoutingV2 operator, which implements initial expert routing for Mixture-of-Experts (MoE) models on Ascend NPUs. This is version 2 of the routing initialization.

## Technical Significance
MoE routing initialization determines which experts process which tokens, a critical operation for MoE model efficiency. MoeInitRoutingV2 likely improves upon the original with better load balancing, faster computation, or support for newer MoE patterns, enabling scalable MoE inference.

## Related
- `kernel-moe`
- `kernel-topk`
- `technique-bank-conflict-avoidance`
- `hw-vector-unit`