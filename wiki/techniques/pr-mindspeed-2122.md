---
id: technique-pr-mindspeed-2122
title: "PR Insight: Ascend/MindSpeed #2122"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - optimizer
  - refactor
  - adamw
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2122"
---

# PR Insight: Ascend/MindSpeed #2122

**Title:** refactor: fused_ema_adamw 重构

## Overview
This PR refactors the fused EMA (Exponential Moving Average) AdamW optimizer implementation in MindSpeed. The refactoring affects the optimizer architecture across multiple components including the core optimizer module, op builders, and feature managers for both PyTorch and MindSpore backends.

## Technical Significance
The refactoring improves code maintainability and consistency of the fused EMA AdamW optimizer, which is a critical performance optimization for distributed training. This optimizer fuses EMA updates with AdamW weight updates to reduce memory traffic and improve training efficiency on Ascend NPUs. The refactor likely standardizes interfaces between the PyTorch and MindSpore implementations while preserving the performance benefits of operator fusion.

## Related
- `technique-operator-fusion`
- `technique-hccl-optimization`