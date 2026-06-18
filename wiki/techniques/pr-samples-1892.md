---
id: technique-pr-samples-1892
title: "PR Insight: Ascend/samples #1892"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - leakyrelu
  - operator-fusion
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1892"
---

# PR Insight: Ascend/samples #1892

**Title:** 添加MatmulLeakyrelu算子样例

## Overview
This PR adds a fused MatMul + LeakyReLU operator sample, demonstrating how to fuse matrix multiplication with an activation function to reduce memory transfers and improve performance.

## Technical Significance
Showcases operator fusion patterns on Ascend hardware, where combining multiple operations into a single kernel eliminates intermediate data movement and enables better utilization of on-chip memory and compute units.

## Related
- `technique-operator-fusion`
- `kernel-matmul-ascendc`