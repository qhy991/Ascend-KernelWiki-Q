---
id: technique-pr-samples-2005
title: "PR Insight: Ascend/samples #2005"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - edge-handling
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2005"
---

# PR Insight: Ascend/samples #2005

**Title:** 修改MatMul尾块计算逻辑

## Overview
This PR modifies the MatMul sample to handle edge cases where matrix dimensions are not evenly divisible by tile sizes, ensuring correct computation of partial (tail) blocks at matrix boundaries.

## Technical Significance
Improves MatMul robustness by properly handling non-tiling-friendly dimensions, ensuring numerical correctness for all input sizes. This is a common challenge in matrix operations and the fix demonstrates proper edge case handling.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`