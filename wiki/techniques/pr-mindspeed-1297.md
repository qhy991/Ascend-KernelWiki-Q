---
id: technique-pr-mindspeed-1297
title: "PR Insight: Ascend/MindSpeed #1297"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - gmm
  - bugfix
  - matmul
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1297"
---

# PR Insight: Ascend/MindSpeed #1297

**Title:** bugfix_GmmAdd_MmAdd

## Overview
This PR fixes bugs in GMM (General Matrix Multiplication) Add and MM (Matrix Multiplication) Add operations. These are fused operator patterns commonly used in neural network layers that combine matrix multiplication with element-wise additions.

## Technical Significance
Correctness bugs in fused GMM/MM-Add operators can cause numerical errors or incorrect model outputs. The fix ensures proper behavior of these fused operations on Ascend hardware, which is critical for models relying on efficient fused implementations like attention mechanisms or MLP layers.

## Related
- technique-operator-fusion
- kernel-matmul
- kernel-elementwise