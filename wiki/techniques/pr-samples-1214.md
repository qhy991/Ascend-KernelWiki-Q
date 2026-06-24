---
id: technique-pr-samples-1214
title: "PR Insight: Ascend/samples #1214"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - samples
  - conv2d
  - tbe-tik
  - platform-support
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1214"
---

# PR Insight: Ascend/samples #1214

**Title:** Conv2dTik support sd3403

## Overview
This PR adds support for the SD3403 platform to the Conv2dTik sample, which implements Conv2D using TBE TIK (Tensor Boost Engine Tensor Instruction Kernel).

## Technical Significance
Adding platform support for Conv2D requires adapting to SD3403's hardware characteristics, including memory size, compute unit capabilities, and operator support. Conv2D is a fundamental operation in CNNs and benefits significantly from Ascend's cube unit for matrix multiplication and efficient memory tiling strategies.

## Related
- kernel-matmul
- wiki-hardware-cube-unit
- technique-tiling
- technique-nz-tiling