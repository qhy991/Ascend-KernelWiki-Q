---
id: technique-pr-mindspeed-1220
title: "PR Insight: Ascend/MindSpeed #1220"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - gmm
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1220"
---

# PR Insight: Ascend/MindSpeed #1220

**Title:** gmm builder fix bug

## Overview
This PR fixes a bug in the GMM (General Matrix Multiplication) builder, which is responsible for constructing or configuring GMM operations. The builder pattern is used to set up matrix multiplication kernels with appropriate parameters and optimizations.

## Technical Significance
Correct GMM configuration is essential for optimal performance on Ascend's Cube unit. This bug fix ensures that matrix multiplication operations are built with the right parameters (tiling, formats, data paths) for efficient execution on Ascend NPUs.

## Related
- kernel-matmul
- hw-cube-unit