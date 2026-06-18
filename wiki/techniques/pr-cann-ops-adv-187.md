---
id: technique-pr-cann-ops-adv-187
title: "PR Insight: cann-ops-adv #187"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - topk
  - refactoring
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/187"
---

# PR Insight: cann-ops-adv #187 - delete op FusedAddTopkDiv

## Overview
This PR removes the FusedAddTopkDiv operator, likely refactoring the MoE routing computation to use alternative implementations or decomposed operations.

## Technical Significance
Removing a fused operator may indicate that the fusion was not beneficial for performance or maintenance. The refactor likely simplifies the codebase or moves to better patterns, improving code quality and potentially enabling other optimizations for MoE routing on Ascend NPUs.

## Related
- `kernel-moe`
- `kernel-topk`
- `technique-operator-fusion`
- `hw-vector-unit`