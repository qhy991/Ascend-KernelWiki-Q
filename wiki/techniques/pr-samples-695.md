---
id: technique-pr-samples-695
title: "PR Insight: Ascend/samples #695"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - opencv
  - cmake
  - build-system
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/695"
---

# PR Insight: Ascend/samples #695

**Title:** 更新opencv安装的cmake 参数

## Overview
This PR updates the CMake parameters used for OpenCV installation in the samples repository, improving the build configuration and enabling or disabling specific OpenCV features.

## Technical Significance
Updating OpenCV installation parameters ensures samples use the optimal OpenCV configuration for Ascend development, balancing feature availability with build time and binary size. This can also resolve compatibility issues with specific OpenCV versions.

## Related
- N/A (build configuration)