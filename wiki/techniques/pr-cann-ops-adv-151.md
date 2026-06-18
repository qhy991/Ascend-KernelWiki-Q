---
id: technique-pr-cann-ops-adv-151
title: "PR Insight: cann-ops-adv #151"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/151"
---

# PR Insight: cann-ops-adv #151 - add moe_finalize_routing_v2_grad

## Overview
This PR adds the moe_finalize_routing_v2_grad operator, which computes gradients for version 2 of the MoE routing finalization during backpropagation, supporting MoE model training.

## Technical Significance
Gradients through routing finalization complete the gradient flow path through the MoE routing process. This operator ensures correct gradient computation for the final routing operations on Ascend NPUs, enabling end-to-end MoE training.

## Related
- `kernel-moe`
- `kernel-reduce`
- `hw-vector-unit`
- `technique-atomic-accumulation`