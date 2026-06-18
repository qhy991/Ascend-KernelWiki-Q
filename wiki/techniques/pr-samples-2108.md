---
id: technique-pr-samples-2108
title: "PR Insight: Ascend/samples #2108"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - build
  - cmake
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2108"
---

# PR Insight: Ascend/samples #2108

**Title:** 更新cmake脚本

## Overview
This PR updates the CMake build scripts used for compiling AscendC sample applications. The changes may include dependency path updates, new compiler flags, or build system improvements to align with updated CANN toolchains.

## Technical Significance
CMake scripts control compilation flags that impact kernel optimization (e.g., -O3, vectorization settings). Build script updates ensure samples compile correctly with new CANN versions and may expose new optimization flags or fix compilation issues with AscendC operators.

## Related
- `technique-ascendc`