---
id: technique-pr-samples-891
title: "PR Insight: Ascend/samples #891"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - build
  - cmake
  - header-files
  - presenter
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/891"
---

# PR Insight: Ascend/samples #891

**Title:** 修复编译时找不到presenter agent相关的头文件

## Overview
This PR fixes a compilation error where the build system could not find header files related to the presenter agent. The fix likely adjusts CMake include directories or header file paths to resolve the missing dependency.

## Technical Significance
Header file path issues are common build system problems that can block compilation. This fix ensures that samples using the presenter agent (Ascend's visualization/display component for inference results) can compile successfully. It demonstrates proper CMake configuration for including external dependencies in CANN projects.

## Related
- CMake include directory configuration
- Presenter agent header file organization
- Build system dependency resolution
- Presenter agent API usage