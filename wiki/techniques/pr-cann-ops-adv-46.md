---
id: technique-pr-cann-ops-adv-46
title: "PR Insight: cann-ops-adv #46"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - flash-attention
  - attention
  - bugfix
  - correctness
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/46"
---

# PR Insight: cann-ops-adv #46 - FA/FAG Bugfix

## Overview
This PR fixes bugs in the FA (FlashAttention) and FAG (FlashAttentionScoreGrad) operators, addressing correctness issues in attention computation and gradient calculation.

## Technical Significance
Correctness bugs in attention operators can lead to incorrect model outputs or training instability. This fix ensures that attention scores and gradients are computed accurately, which is critical for model quality and training convergence on Ascend NPUs.

## Related
- `kernel-flash-attention`
- `kernel-attention`
- `technique-online-softmax`