---
id: technique-pr-sgl-kernel-npu-24
title: "PR Insight: sgl-project/sgl-kernel-npu #24"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - build
  - deepep
  - cmake
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/24"
---

# PR Insight: sgl-project/sgl-kernel-npu #24

**Title:** fix deepep cmakelist bug

## Overview
This PR fixes a bug in the Deep EP CMakeLists.txt configuration file that was causing build issues. The fix involves correcting dependency or target linking problems in the CMake configuration.

## Technical Significance
Resolves build system issues that prevent successful compilation of Deep EP kernels on Ascend. Proper CMake configuration is essential for integrating with Ascend CANN build toolchains and ensuring correct library linking for kernel operators.

## Related
- technique-build-configuration
- technique-cmake