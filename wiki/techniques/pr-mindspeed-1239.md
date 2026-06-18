---
id: technique-pr-mindspeed-1239
title: "PR Insight: Ascend/MindSpeed #1239"
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
  - "https://gitee.com/ascend/MindSpeed/pulls/1239"
---

# PR Insight: Ascend/MindSpeed #1239

**Title:** 【master】【bugfix】修复激活函数重计算bug

## Overview
This PR fixes a bug in activation function recomputation logic. Recomputation trades compute for memory by recalculating activations during backward passes instead of storing them from forward passes.

## Technical Significance
Activation recomputation is a key memory optimization for training large models on Ascend NPUs. This bug fix ensures correct recomputation behavior, preventing incorrect gradients or wasted memory that could prevent training large models effectively.

## Related
- technique-data-reuse
- technique-memory-optimization