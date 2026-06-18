---
id: technique-pr-catlass-178
title: "PR Insight: Ascend/catlass #178"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - preload
  - zN-format
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/178"
---

# PR Insight: Ascend/catlass #178

**Title:** 新增21_basic_matmul_preload_zN

## Overview
This PR adds a new example demonstrating basic matmul with Z-matrix preload in zN format. It shows how to optimize data loading for the right operand in matrix multiplication.

## Technical Significance
Preloading the Z matrix in zN format reduces data movement overhead by keeping operands in optimal formats for the cube unit. This optimization improves memory bandwidth utilization and reduces latency for matmul operations.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`
- `technique-double-buffering`