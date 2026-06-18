---
id: technique-pr-mindspeed-2427
title: "PR Insight: Ascend/MindSpeed #2427"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - test
  - optimizer
  - adamw
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2427"
---

# PR Insight: Ascend/MindSpeed #2427

**Title:** test: add ut for fused_ema_adamw

## Overview
This PR adds unit tests for the fused_ema_adamw optimizer. Fused EMA (Exponential Moving Average) with AdamW optimizer combines parameter updates and EMA maintenance in a single kernel for better performance.

## Technical Significance
Validates the correctness of fused optimizer operations on Ascend NPUs. Fused optimizers reduce kernel launch overhead and improve memory bandwidth utilization by combining multiple operations into a single kernel.

## Related
- `technique-operator-fusion`
- `kernel-elementwise-ascendc`