---
id: technique-pr-samples-2034
title: "PR Insight: Ascend/samples #2034"
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
  - "https://gitee.com/ascend/samples/pulls/2034"
---

# PR Insight: Ascend/samples #2034

**Title:** modify cmake

## Overview
This PR modifies CMake build configuration for AscendC sample applications. The changes may affect build paths, dependency resolution, or compilation flags.

## Technical Significance
Build system modifications ensure samples compile correctly with various CANN versions and development environments. CMake changes may expose new compiler optimization flags or fix build issues that prevent developers from running sample code.

## Related
- `technique-ascendc`