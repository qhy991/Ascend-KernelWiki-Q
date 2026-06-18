---
id: technique-pr-cann-ops-adv-248
title: "PR Insight: Ascend/cann-ops-adv #248"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - softmax
  - transformer
  - ascendc
  - operator-fusion
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/248"
---

# PR Insight: Ascend/cann-ops-adv #248

**Title:** moodify aclnnScaledMaskedSoftmaxGrad to aclnnScaledMaskedSoftmaxBackward

## Overview
This PR modifies the API naming convention for the scaled masked softmax gradient operator, changing from `aclnnScaledMaskedSoftmaxGrad` to `aclnnScaledMaskedSoftmaxBackward`. The change affects the high-level API wrapper for the scaled masked softmax gradient computation in transformer models, standardizing the naming to follow the backward pass convention used across other operators.

## Technical Significance
The naming standardization improves API consistency and developer experience by following the "Backward" suffix convention for gradient operators. This change affects the operator host implementation at `src/transformer/scaled_masked_softmax_grad_v2/ophost/aclnn_scaled_masked_softmax_backward.cpp` and ensures uniform naming patterns across the CANN operator library, making the API more predictable for developers working with transformer attention mechanisms.

## Related
- `technique-softmax-ascendc`
- `technique-transformer-attention`