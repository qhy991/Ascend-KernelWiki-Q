---
id: technique-pr-cann-ops-adv-171
title: "PR Insight: cann-ops-adv #171"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - softmax
  - gradient
  - attention
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/171"
---

# PR Insight: cann-ops-adv #171 - add scaled_masked_softmaxgrad_v2

## Overview
This PR adds version 2 of the scaled_masked_softmax_grad operator, which computes gradients for scaled masked softmax operations used in attention mechanisms.

## Technical Significance
Scaled masked softmax gradients are essential for attention backpropagation. Version 2 likely includes performance improvements, better numerical stability, or support for additional masking patterns, enabling efficient transformer training on Ascend NPUs.

## Related
- `kernel-softmax`
- `kernel-attention`
- `technique-online-softmax`
- `hw-vector-unit`