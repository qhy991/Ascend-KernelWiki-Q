---
id: technique-pr-mindspeed-2370
title: "PR Insight: Ascend/MindSpeed #2370"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - gloo
  - ema
  - optimizer
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2370"
---

# PR Insight: Ascend/MindSpeed #2370

**Title:** fix compatibility issue between disable gloo and ema optim

## Overview
This PR fixes a compatibility issue between disabling gloo and EMA (Exponential Moving Average) optimizer. The issue likely arises from communication backend dependencies in the EMA implementation.

## Technical Significance
Ensures EMA optimizer works correctly when gloo is disabled and HCCL is used. EMA is commonly used for better model generalization, and proper backend compatibility is essential for distributed training.

## Related
- `technique-hccl-optimization`
- `technique-distributed-training`
- `technique-optimizer-fusion`