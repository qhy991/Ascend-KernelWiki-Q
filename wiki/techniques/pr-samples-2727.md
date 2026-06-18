---
id: technique-pr-samples-2727
title: "PR Insight: Ascend/samples #2727"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - leakyrelu
  - ascendc
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2727"
---

# PR Insight: Ascend/samples #2727

**Title:** add matmulleakyrelu sample

## Overview
This PR adds a new sample implementation of matrix multiplication fused with LeakyReLU activation using AscendC. The sample demonstrates how to combine GEMM computation with element-wise activation in a single kernel.

## Technical Significance
Fusing matmul with LeakyReLU reduces memory traffic by avoiding intermediate storage and enables better pipelining between computation stages. This optimization is particularly valuable for transformer models and neural networks that commonly use this activation function.

## Related
- kernel-matmul-ascendc
- technique-operator-fusion
- pr-samples-2713