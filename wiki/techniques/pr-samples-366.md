---
id: technique-pr-samples-366
title: "PR Insight: Ascend/samples #366"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - custom-op
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/366"
---

# PR Insight: Ascend/samples #366

**Title:** matmul

## Overview
This PR adds or updates the matrix multiplication (matmul) custom operator sample, demonstrating how to implement efficient matmul kernels using TBE/TIK interfaces on Ascend hardware.

## Technical Significance
Provides a reference implementation for matmul, the most fundamental operation in deep learning workloads. It shows optimal utilization of the Cube unit and proper tiling strategies for matrix operations on Ascend NPUs.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`
- `technique-cube-vector-overlap`