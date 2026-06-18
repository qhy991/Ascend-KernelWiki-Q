---
id: technique-pr-cann-ops-adv-164
title: "PR Insight: cann-ops-adv #164"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - sinkhorn
  - load-balancing
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-ops-adv/pulls/164"
---

# PR Insight: cann-ops-adv #164 - add sinkhorn operator

## Overview
This PR adds a Sinkhorn operator for Sinkhorn-Knopp iteration, used for load balancing in MoE models by optimizing expert assignment through matrix scaling.

## Technical Significance
Sinkhorn iteration provides an alternative to softmax-based gating for MoE routing, offering better load balancing through matrix scaling iterations. This operator enables Sinkhorn-based routing on Ascend NPUs, supporting advanced load balancing strategies for large-scale MoE models.

## Related
- `kernel-moe`
- `kernel-softmax`
- `technique-load-balancing`
- `hw-vector-unit`