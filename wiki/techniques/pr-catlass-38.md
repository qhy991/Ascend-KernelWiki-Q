---
id: technique-pr-catlass-38
title: "PR Insight: Ascend/catlass #38"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - grouped-matmul
  - testing
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/38"
---

# PR Insight: Ascend/catlass #38

**Title:** 新增GroupedMatmul的结果比较函数

## Overview
This PR adds result comparison functions for GroupedMatmul operations in the catlass library. It introduces testing utilities to verify correctness of grouped matrix multiplication implementations.

## Technical Significance
GroupedMatmul is essential for processing multiple matrix multiplications with different sizes in a single kernel launch. Result comparison functions enable automated validation of correctness, which is critical for tuning and optimization work on Ascend's cube unit.

## Related
- `kernel-matmul-ascendc`