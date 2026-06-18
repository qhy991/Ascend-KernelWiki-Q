---
id: technique-pr-samples-2810
title: "PR Insight: Ascend/samples #2810"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - bugfix
  - ascendc
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2810"
---

# PR Insight: Ascend/samples #2810

**Title:** Fix matmul

## Overview
This PR fixes a bug in a matmul sample implementation. The fix addresses issues that were causing incorrect computation results or runtime errors in the matrix multiplication kernel.

## Technical Significance
Correct matrix multiplication is fundamental to most neural network computations. Ensuring matmul samples work correctly is essential because they serve as reference implementations for developers building custom GEMM kernels.

## Related
- kernel-matmul-ascendc
- technique-cube-vector-overlap