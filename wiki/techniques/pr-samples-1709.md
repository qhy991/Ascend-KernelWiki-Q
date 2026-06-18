---
id: technique-pr-samples-1709
title: "PR Insight: Ascend/samples #1709"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolov7
  - cmake
  - build
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1709"
---

# PR Insight: Ascend/samples #1709

**Title:** 修改案例sampleYOLOV7MultiInput CMakeLists.txt问题

## Overview
This PR fixes issues in the CMakeLists.txt configuration file for the YOLOV7MultiInput sample case, resolving build or linking problems.

## Technical Significance
CMake configuration errors can prevent samples from compiling successfully. Fixing build configuration issues ensures developers can build and run samples without encountering CMake-related errors, which is particularly important for complex multi-input samples.

## Related
- technique-build-system