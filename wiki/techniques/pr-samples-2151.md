---
id: technique-pr-samples-2151
title: "PR Insight: Ascend/samples #2151"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - build
  - cmake
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2151"
---

# PR Insight: Ascend/samples #2151

**Title:** fix CmakeList bug

## Overview
This PR fixes a bug in CMakeLists.txt build configuration files, ensuring proper compilation and linking of sample code.

## Technical Significance
Correct build configuration is essential for the samples repository to work across different environments and Ascend toolkit versions. Build system bugs prevent users from successfully compiling and running samples.

## Related