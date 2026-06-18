---
id: technique-pr-samples-1277
title: "PR Insight: Ascend/samples #1277"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - tensorflow
  - elementwise
  - scatter
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1277"
---

# PR Insight: Ascend/samples #1277

**Title:** 【TF2.6】TF2.6资料新增add/scatter_nd_add代码实例

## Overview
This PR adds TensorFlow 2.6 code examples for the add and scatter_nd_add operators to the samples repository. These are fundamental elementwise and scatter operations commonly used in neural network workloads.

## Technical Significance
Adding TF2.6 examples for add and scatter_nd_add provides developers with Ascend-specific implementations for these operators. The add operator is a basic elementwise operation that benefits from vector unit optimization, while scatter_nd_add involves indexing patterns that may require careful memory access optimization on Ascend's unified buffer architecture.

## Related
- kernel-elementwise
- technique-vector-unit
- hw-unified-buffer