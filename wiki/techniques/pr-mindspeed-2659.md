---
id: technique-pr-mindspeed-2659
title: "PR Insight: Ascend/MindSpeed #2659"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - initialization
  - gpu
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2659"
---

# PR Insight: Ascend/MindSpeed #2659

**Title:** fix: correct parameter naming in _initialize_affine_weight_gpu

## Overview
This PR corrects parameter naming in the `_initialize_affine_weight_gpu` function. The fix addresses incorrect parameter names that could cause issues during model weight initialization on GPU devices.

## Technical Significance
Proper weight initialization is critical for training convergence and numerical stability. This fix ensures that affine weights are correctly initialized with the proper scaling factors and dtypes, preventing potential training issues or performance degradation.

## Related