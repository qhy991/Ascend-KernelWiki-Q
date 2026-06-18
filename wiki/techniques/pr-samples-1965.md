---
id: technique-pr-samples-1965
title: "PR Insight: Ascend/samples #1965"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - opapi
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1965"
---

# PR Insight: Ascend/samples #1965

**Title:** 修改opapi头文件路径，新增MatMul简易工程

## Overview
This PR updates the OpAPI header file paths to match the latest CANN SDK structure and adds a simplified MatMul project that demonstrates minimal setup for matrix multiplication.

## Technical Significance
Improves accessibility of operator development by providing a minimal MatMul example, making it easier for new developers to get started with AscendC programming without navigating complex project structures.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`