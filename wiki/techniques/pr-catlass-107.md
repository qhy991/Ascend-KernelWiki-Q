---
id: technique-pr-catlass-107
title: "PR Insight: Ascend/catlass #107"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - bias
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/107"
---

# PR Insight: Ascend/catlass #107

**Title:** 新增matmul bias

## Overview
This PR adds bias addition support to matmul operations in catlass. It enables fused matrix multiplication with bias addition operations on Ascend hardware.

## Technical Significance
Bias addition is a common operation in neural network layers (e.g., linear layers, attention). Fusing it with matmul reduces kernel launch overhead and enables better use of the unified buffer for intermediate results, improving overall inference performance.

## Related
- `kernel-matmul-ascendc`
- `technique-operator-fusion`