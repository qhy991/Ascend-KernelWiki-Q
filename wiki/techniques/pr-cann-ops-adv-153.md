---
id: technique-pr-cann-ops-adv-153
title: "PR Insight: cann-ops-adv #153"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/153"
---

# PR Insight: cann-ops-adv #153 - add moe_finalize_routing

## Overview
This PR adds the moe_finalize_routing operator, which completes the routing process for Mixture-of-Experts models by finalizing routing decisions and preparing outputs.

## Technical Significance
Finalizing routing handles post-processing of expert routing decisions. This operator includes operations like token unpermutation, expert output aggregation, and routing statistics collection, completing the MoE forward pass on Ascend NPUs.

## Related
- `kernel-moe`
- `kernel-reduce`
- `hw-vector-unit`
- `technique-atomic-accumulation`