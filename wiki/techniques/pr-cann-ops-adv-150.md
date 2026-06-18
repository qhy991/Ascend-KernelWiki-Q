---
id: technique-pr-cann-ops-adv-150
title: "PR Insight: cann-ops-adv #150"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - ascendc
  - reduce
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/150"
---

# PR Insight: cann-ops-adv #150 - add moe_compute_expert_tokens

## Overview
This PR adds the moe_compute_expert_tokens operator, which computes the number of tokens assigned to each expert in MoE models for load balancing and capacity management.

## Technical Significance
Tracking expert token counts is essential for MoE load balancing and capacity planning. This operator provides the necessary statistics for dynamic expert capacity adjustment and load balancing strategies, improving MoE inference efficiency on Ascend NPUs.

## Related
- `kernel-moe`
- `kernel-reduce`
- `hw-vector-unit`
- `technique-workspace-management`