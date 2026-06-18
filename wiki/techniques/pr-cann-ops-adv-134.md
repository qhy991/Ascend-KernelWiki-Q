---
id: technique-pr-cann-ops-adv-134
title: "PR Insight: cann-ops-adv #134"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - ascendc
  - gradient
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/134"
---

# PR Insight: cann-ops-adv #134 - MoeTokenUnpermuteGrad open source

## Overview
This PR open-sources the MoeTokenUnpermuteGrad operator, which computes gradients for the token unpermutation operation in MoE models during backpropagation.

## Technical Significance
Gradient computation for token permutation/unpermutation is critical for training MoE models. This operator enables efficient gradient flow through the routing process, supporting MoE model training on Ascend NPUs with correct backpropagation through expert assignment.

## Related
- `kernel-moe`
- `technique-data-reuse`
- `hw-mte`
- `hw-unified-buffer`