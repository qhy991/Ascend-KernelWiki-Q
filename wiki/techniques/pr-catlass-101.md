---
id: technique-pr-catlass-101
title: "PR Insight: Ascend/catlass #101"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - gemm
  - device-layer
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/101"
---

# PR Insight: Ascend/catlass #101

**Title:** 0517 device-gemm PR

## Overview
This PR adds or updates device-layer support for GEMM operations in catlass. It extends device-side abstractions for general matrix multiplication kernels.

## Technical Significance
Device-layer GEMM abstractions enable more flexible kernel composition and better integration with operator fusion pipelines. This is important for complex workloads where multiple matmul operations need to be scheduled efficiently on the cube unit.

## Related
- `kernel-matmul-ascendc`
- `technique-cube-vector-overlap`