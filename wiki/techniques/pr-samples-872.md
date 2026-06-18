---
id: technique-pr-samples-872
title: "PR Insight: Ascend/samples #872"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - cmake
  - build
  - dependency
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/872"
---

# PR Insight: Ascend/samples #872

**Title:** 删除sample中CMAKELIST依赖路径

## Overview
This PR removes CMakeLists dependency paths from samples. The change likely eliminates hardcoded paths or unnecessary find_package calls, making the build configuration more portable and robust.

## Technical Significance
Hardcoded dependency paths in CMakeLists files cause portability issues across different development environments. Removing these paths improves build system reliability and makes samples easier to compile on different machines. This demonstrates best practices for CMake configuration in CANN projects, using proper find_package mechanisms instead of absolute paths.

## Related
- CMake dependency management best practices
- Portable build configuration
- CANN environment setup
- Build system simplification