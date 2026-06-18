---
id: technique-pr-catlass-176
title: "PR Insight: Ascend/catlass #176"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - ascendc
  - debugging
  - dump
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/176"
---

# PR Insight: Ascend/catlass #176

**Title:** 支持AscendC::Dump/printf

## Overview
This PR adds support for AscendC::Dump and printf debugging functionality. It enhances kernel debugging capabilities for catlass on Ascend hardware.

## Technical Significance
Kernel debugging is essential for developing and optimizing complex matmul and attention kernels. Dump and printf support enable developers to inspect tensor values and trace execution flow, which is critical for debugging cube unit pipelines and memory access patterns.

## Related
- `kernel-matmul-ascendc`
- `hw-cube-unit`
- `technique-bank-conflict-avoidance`