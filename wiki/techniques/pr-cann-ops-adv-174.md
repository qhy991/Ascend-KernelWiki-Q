---
id: technique-pr-cann-ops-adv-174
title: "PR Insight: cann-ops-adv #174"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/174"
---

# PR Insight: cann-ops-adv #174 - add op moeinitrouting

## Overview
This PR adds the MoeInitRouting operator, which implements initial expert routing for Mixture-of-Experts models on Ascend NPUs.

## Technical Significance
MoE routing initialization determines which experts process which tokens, a critical operation for MoE model efficiency. This operator provides the foundation for expert selection on Ascend NPUs with optimized memory access patterns and load balancing.

## Related
- `kernel-moe`
- `kernel-topk`
- `technique-bank-conflict-avoidance`
- `hw-vector-unit`