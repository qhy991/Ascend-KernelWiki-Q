---
id: technique-pr-samples-1991
title: "PR Insight: Ascend/samples #1991"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - leakyrelu
  - pybind
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1991"
---

# PR Insight: Ascend/samples #1991

**Title:** 新增pybind调用MatMulLeakyrelu样例

## Overview
This PR adds a pybind11-based Python interface for the MatMulLeakyReLU fused operator, enabling Python-based applications to invoke this optimized kernel without writing C++ host code.

## Technical Significance
Demonstrates how to expose fused custom operators to Python, showing the complete pattern from kernel implementation to pybind bindings. This is essential for integrating optimized operators into PyTorch/TensorFlow custom ops.

## Related
- `technique-operator-fusion`
- `kernel-matmul-ascendc`