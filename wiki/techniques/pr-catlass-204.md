---
id: technique-pr-catlass-204
title: "PR Insight: Ascend/catlass #204"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - activation
  - elementwise
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/204"
---

# PR Insight: Ascend/catlass #204

**Title:** 【26, 27, 28】新增matmul relu, gelu, swish算子

## Overview
This PR adds matmul operators fused with activation functions including ReLU, GELU, and Swish. It enables end-to-end matrix multiplication with non-linear activation on Ascend hardware.

## Technical Significance
Fusing activation functions with matmul eliminates separate kernel launches and reduces memory traffic. This optimization is essential for transformer architectures where matmul-activation patterns are ubiquitous, significantly improving inference throughput.

## Related
- `kernel-matmul-ascendc`
- `technique-operator-fusion`
- `kernel-elementwise-ascendc`