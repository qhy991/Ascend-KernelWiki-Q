---
id: technique-pr-samples-623
title: "PR Insight: Ascend/samples #623"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - matmul
  - elementwise
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/623"
---

# PR Insight: Ascend/samples #623

**Title:** AddMatMatElements

## Overview
This PR adds a sample for matrix-matrix element operations (AddMatMatElements), demonstrating how to implement element-wise arithmetic operations between two matrices on Ascend hardware using AscendC or TBE operators.

## Technical Significance
Matrix element operations are fundamental building blocks for many neural network operations. Having reference implementations shows efficient patterns for leveraging Ascend's vector unit for element-wise computations, which is critical for custom operator development.

## Related
- kernel-matmul-ascendc
- elementwise operations
- Vector unit usage
- Custom operators