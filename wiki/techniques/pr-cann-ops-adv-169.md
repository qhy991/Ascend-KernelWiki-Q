---
id: technique-pr-cann-ops-adv-169
title: "PR Insight: cann-ops-adv #169"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/169"
---

# PR Insight: cann-ops-adv #169 - permuteGrad op

## Overview
This PR adds a permutation gradient operator, which computes gradients for token permutation/unpermutation operations used in MoE models during backpropagation.

## Technical Significance
Gradient computation through permutation operations is essential for training MoE models correctly. This operator ensures accurate gradient flow through token reordering on Ascend NPUs, supporting end-to-end MoE model training.

## Related
- `kernel-moe`
- `technique-data-reuse`
- `hw-mte`
- `hw-unified-buffer`