---
id: technique-pr-catlass-39
title: "PR Insight: Ascend/catlass #39"
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
  - "https://gitee.com/ascend/catlass/pulls/39"
---

# PR Insight: Ascend/catlass #39

**Title:** device分支新增GroupedMatmul的结果比较函数

## Overview
This PR adds GroupedMatmul result comparison functions to the device branch of catlass. It extends testing infrastructure for device-side grouped matrix multiplication operations.

## Technical Significance
Device-side comparison functions enable inline validation of correctness during kernel execution, which is valuable for debugging and optimizing AscendC matmul implementations on the NPU device.

## Related
- `kernel-matmul-ascendc`