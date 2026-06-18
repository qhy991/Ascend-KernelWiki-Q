---
id: technique-pr-cann-ops-adv-132
title: "PR Insight: cann-ops-adv #132"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/132"
---

# PR Insight: cann-ops-adv #132 - add_moe_finalize_routing_v2

## Overview
This PR adds the moe_finalize_routing_v2 operator, which completes the routing process for Mixture-of-Experts models by finalizing routing decisions and preparing outputs.

## Technical Significance
Finalizing routing is the complement to initialization, handling the post-processing of expert routing decisions. This operator likely includes operations like token unpermutation, expert output aggregation, and routing statistics collection for load balancing.

## Related
- `kernel-moe`
- `kernel-reduce`
- `hw-vector-unit`
- `technique-atomic-accumulation`