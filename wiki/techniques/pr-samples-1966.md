---
id: technique-pr-samples-1966
title: "PR Insight: Ascend/samples #1966"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - tiling
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1966"
---

# PR Insight: Ascend/samples #1966

**Title:** 修改MatMul初始化Tiling方式

## Overview
This PR modifies how MatMul initializes tiling parameters, improving the strategy for partitioning matrices to optimize cache usage and minimize global memory accesses.

## Technical Significance
Optimizes tiling strategy for MatMul operations, showing how to calculate optimal tile sizes based on matrix dimensions and available on-chip memory. Proper tiling is critical for achieving high performance on Ascend hardware.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`
- `technique-double-buffering`