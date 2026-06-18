---
id: technique-pr-catlass-123
title: "PR Insight: Ascend/catlass #123"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - ascendc
  - debugging
  - printf
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/123"
---

# PR Insight: Ascend/catlass #123

**Title:** 使能AscendC::DumpTensor/AscendC::printf

## Overview
This PR enables AscendC debugging utilities including DumpTensor and printf functions. It facilitates debugging and verification of kernel operations on Ascend NPUs.

## Technical Significance
Debugging NPU kernels is challenging without proper instrumentation. Enabling DumpTensor and printf allows developers to inspect intermediate values and trace execution, which is essential for optimizing complex matmul and attention kernels on the cube unit.

## Related
- `kernel-matmul-ascendc`
- `hw-cube-unit`