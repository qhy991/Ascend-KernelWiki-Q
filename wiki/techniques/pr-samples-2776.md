---
id: technique-pr-samples-2776
title: "PR Insight: Ascend/samples #2776"
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
  - "https://gitee.com/ascend/samples/pulls/2776"
---

# PR Insight: Ascend/samples #2776

**Title:** add simple pybind sample && matmul leakyrelu sample

## Overview
This PR adds two new samples: a simple PyBind11 sample for Python integration, and a matmul leakyrelu sample. The PyBind sample demonstrates how to expose AscendC operators to Python, while the matmul leakyrelu sample shows fused GEMM with activation.

## Technical Significance
PyBind integration is crucial for making AscendC kernels accessible from Python frameworks like PyTorch and TensorFlow. Combined with the matmul leakyrelu sample, this provides a complete reference for implementing and deploying custom operators in Python-based ML pipelines.

## Related
- kernel-matmul-ascendc
- technique-operator-fusion
- pr-samples-2727