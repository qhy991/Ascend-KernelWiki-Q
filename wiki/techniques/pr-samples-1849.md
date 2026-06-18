---
id: technique-pr-samples-1849
title: "PR Insight: Ascend/samples #1849"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - build
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1849"
---

# PR Insight: Ascend/samples #1849

**Title:** 更新cmakelist路径

## Overview
This PR updates CMakeLists.txt file paths in a sample application. CMake is used to configure the build process for C/C++ applications in the Ascend ecosystem.

## Technical Significance
Correct build configuration is essential for successfully compiling and linking Ascend applications. Updating CMakeLists paths ensures samples can be built on different development environments and maintains compatibility with the latest CANN toolkit versions.

## Related
- `wiki-technique-build`