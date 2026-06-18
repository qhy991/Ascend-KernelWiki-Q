---
id: technique-pr-mindspeed-1053
title: "PR Insight: Ascend/MindSpeed #1053"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - mlp
  - matmul
  - fusion
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1053"
---

# PR Insight: Ascend/MindSpeed #1053

**Title:** mlp适配matmul_add

## Overview
This PR adapts MLP (Multi-Layer Perceptron) layers to use matmul_add fused operations. The fusion combines matrix multiplication with element-wise addition, a common pattern in MLP computations.

## Technical Significance
Using fused matmul_add operations in MLP layers improves performance on Ascend NPUs by reducing memory bandwidth and kernel launch overhead. This adaptation ensures MLP computations leverage Ascend's compute capabilities efficiently while maintaining compatibility with MindSpeed's optimization pipeline.

## Related
- technique-operator-fusion
- kernel-matmul
- kernel-elementwise