---
id: technique-pr-samples-925
title: "PR Insight: Ascend/samples #925"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - cmake
  - build
  - compilation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/925"
---

# PR Insight: Ascend/samples #925

**Title:** 修改IRBuild的 CMakeLists.txt ，缺省状态下可以编译通过

## Overview
This PR modifies the CMakeLists.txt file for the IRBuild sample to ensure successful compilation in default configuration. The change fixes build configuration issues that previously prevented out-of-the-box compilation.

## Technical Significance
Fixing build configuration in samples is critical for developer onboarding. This change ensures that users can compile the IRBuild sample without manual configuration, reducing the learning curve for Ascend CANN development. It likely involves adjusting CMake find_package paths, dependency ordering, or compiler flags.

## Related
- Build system patterns for Ascend samples
- CMake configuration for CANN projects
- IRBuild operator development workflow