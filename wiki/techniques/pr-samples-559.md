---
id: technique-pr-samples-559
title: "PR Insight: Ascend/samples #559"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aicpu
  - cmake
  - build-system
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/559"
---

# PR Insight: Ascend/samples #559

**Title:** fix aicpu cmake

## Overview
This PR fixes a CMake build configuration issue related to AICPU (AI CPU) operator samples. The fix addresses build errors that prevent proper compilation of AICPU operator implementations.

## Technical Significance
Resolves build system issues that block developers from building and running AICPU operator samples. Proper CMake configuration is essential for compiling custom operators that leverage both CPU and NPU acceleration on Ascend platforms.

## Related
- `pattern-build-system`
- `technique-operator-development`