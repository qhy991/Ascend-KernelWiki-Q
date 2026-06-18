---
id: technique-pr-mindspeed-1079
title: "PR Insight: Ascend/MindSpeed #1079"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - adaptive-cp
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1079"
---

# PR Insight: Ascend/MindSpeed #1079

**Title:** hybrid adaptive-cp bug fix

## Overview
This PR fixes a bug in hybrid adaptive context parallelism (adaptive-cp). Context parallelism distributes sequence processing across devices, and hybrid approaches combine it with other parallelism strategies.

## Technical Significance
Adaptive context parallelism is important for scaling long-sequence model training on Ascend clusters. This bug fix ensures correct behavior of the hybrid adaptive-cp feature, enabling efficient training of models with long sequences on multiple Ascend NPUs.

## Related
- technique-communication-optimization
- kernel-attention