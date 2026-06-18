---
id: technique-pr-mindspeed-1261
title: "PR Insight: Ascend/MindSpeed #1261"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - activation
  - recomputation
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1261"
---

# PR Insight: Ascend/MindSpeed #1261

**Title:** 【master】【bugfix】 激活函数重计算判断没有self.layer_number的情况

## Overview
This PR fixes a bug in activation function recomputation logic when `self.layer_number` is not available. The recomputation feature is used to trade compute for memory during training by recomputing activations instead of storing them.

## Technical Significance
Activation recomputation is a critical memory optimization technique for training large models on Ascend NPUs. This bug fix ensures correct behavior when layer number metadata is missing, preventing crashes or incorrect recomputation patterns that could waste memory or cause incorrect gradients.

## Related
- technique-data-reuse
- technique-memory-optimization