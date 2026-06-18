---
id: technique-pr-mindspeed-2306
title: "PR Insight: Ascend/MindSpeed #2306"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - moe
  - fb-overlap
  - gmm
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2306"
---

# PR Insight: Ascend/MindSpeed #2306

**Title:** 【master】【Feature】moe Fb overlap支持 & 修复prob提前gmm基线bug

## Overview
This PR adds fb-overlap (flash-attention overlap) support for MoE (Mixture of Experts) and fixes a bug in the prob提前gmm baseline. GMM likely refers to Gaussian Mixture Model used in expert routing.

## Technical Significance
Enables flash-attention overlap optimization for MoE models, improving performance by overlapping computation with communication. The GMM bug fix ensures correct expert routing probabilities, which is critical for MoE model accuracy.

## Related
- `kernel-flash-attention`
- `technique-moe`
- `technique-cube-vector-overlap`
- `technique-expert-routing`