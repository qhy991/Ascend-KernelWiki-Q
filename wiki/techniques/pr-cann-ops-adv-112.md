---
id: technique-pr-cann-ops-adv-112
title: "PR Insight: cann-ops-adv #112"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/112"
---

# PR Insight: cann-ops-adv #112 - add Rope op

## Overview
This PR adds a Rope (Rotary Position Embedding) operator to the Ascend CANN ops-adv library. Rope encodes position information into query and key tensors for transformer attention.

## Technical Significance
Rotary Position Embedding is a crucial component for modern transformer models like LLaMA. Adding an optimized Rope operator enables efficient position encoding on Ascend NPUs, avoiding data movement between host and device and improving inference performance.

## Related
- `kernel-rope`
- `kernel-attention`
- `hw-vector-unit`
- `technique-format-conversion`