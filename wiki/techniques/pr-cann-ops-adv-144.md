---
id: technique-pr-cann-ops-adv-144
title: "PR Insight: cann-ops-adv #144"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - gradient
  - ascendc
  - elementwise
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/144"
---

# PR Insight: cann-ops-adv #144 - add RoPE_grad op

## Overview
This PR adds the RoPE_grad operator, which computes gradients for the Rotary Position Embedding operation during backpropagation, enabling training of models with RoPE on Ascend NPUs.

## Technical Significance
Gradients through position embeddings are necessary for training models that use RoPE. This operator ensures correct gradient computation for the RoPE transformation, supporting end-to-end training of modern transformer models on Ascend hardware.

## Related
- `kernel-rope`
- `kernel-attention`
- `hw-vector-unit`
- `technique-format-conversion`