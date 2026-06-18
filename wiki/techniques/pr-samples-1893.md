---
id: technique-pr-samples-1893
title: "PR Insight: Ascend/samples #1893"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - sub
  - elementwise
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1893"
---

# PR Insight: Ascend/samples #1893

**Title:** 添加Sub样例

## Overview
This PR adds a Sub (subtraction) operator sample to the repository. The sample demonstrates how to implement and use the element-wise Sub operation on Ascend hardware using AscendC, showing kernel implementation patterns and integration with inference frameworks.

## Technical Significance
The Sub operator is a fundamental element-wise operation in neural networks, used in residual connections, difference calculations, and various preprocessing steps. This sample provides a reference for implementing element-wise subtraction kernels in AscendC, demonstrating memory access patterns, vector operations, and optimization techniques for Ascend910/910B.

## Related
- `kernel-elementwise`
- `technique-vector-unit`