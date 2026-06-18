---
id: technique-pr-cann-ops-adv-148
title: "PR Insight: cann-ops-adv #148"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - attention
  - ascendc
  - elementwise
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/148"
---

# PR Insight: cann-ops-adv #148 - add ApplyRotaryPosEmb op

## Overview
This PR adds the ApplyRotaryPosEmb operator, which applies Rotary Position Embedding to query and key tensors for transformer attention on Ascend NPUs.

## Technical Significance
ApplyRotaryPosEmb is the actual rotation operation that encodes position information. As a separate operator, it provides flexibility for position embedding application and can be fused with attention operations for end-to-end optimized inference.

## Related
- `kernel-rope`
- `kernel-attention`
- `hw-vector-unit`
- `technique-operator-fusion`