---
id: technique-pr-mindspeed-1288
title: "PR Insight: Ascend/MindSpeed #1288"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - gmm
  - adaptation
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1288"
---

# PR Insight: Ascend/MindSpeed #1288

**Title:** GMM+Add 适配

## Overview
This PR adapts the GMM (General Matrix Multiplication) + ADD fused operator for integration with MindSpeed's optimization pipeline. The adaptation ensures the fused operator works correctly with the framework's tensor formats and compute patterns.

## Technical Significance
Proper adaptation of fused operators is essential for achieving performance benefits on Ascend hardware. This work ensures GMM+ADD operations leverage Ascend's compute units efficiently while maintaining compatibility with MindSpeed's tensor parallelism and other optimizations.

## Related
- technique-operator-fusion
- kernel-matmul
- kernel-elementwise