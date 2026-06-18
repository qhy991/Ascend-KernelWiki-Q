---
id: technique-pr-cann-ops-adv-162
title: "PR Insight: cann-ops-adv #162"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - topk
  - elementwise
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/162"
---

# PR Insight: cann-ops-adv #162 - add op FusedAddTopkDiv

## Overview
This PR adds the FusedAddTopkDiv operator, which fuses element-wise addition, Top-K selection, and division operations commonly used in MoE routing on Ascend NPUs.

## Technical Significance
Fusing these operations reduces kernel launch overhead and memory accesses for MoE routing computations. This operator optimizes the computation of gating probabilities with capacity constraints, improving MoE inference efficiency on Ascend hardware.

## Related
- `kernel-moe`
- `kernel-topk`
- `technique-operator-fusion`
- `hw-vector-unit`