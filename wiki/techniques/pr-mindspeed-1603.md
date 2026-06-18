---
id: technique-pr-mindspeed-1603
title: "PR Insight: Ascend/MindSpeed #1603"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - optimizer
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1603"
---

# PR Insight: Ascend/MindSpeed #1603

**Title:** add ema adamw optimizer

## Overview
This PR adds support for EMA (Exponential Moving Average) with AdamW optimizer. EMA maintains a smoothed version of model weights, which can improve model stability and generalization during training.

## Technical Significance
Provides access to advanced optimization techniques that combine the benefits of AdamW with exponential moving averages. EMA-based optimization can improve training stability and final model quality, particularly beneficial for large-scale training scenarios.

## Related
- `pattern-optimization`