---
id: technique-pr-samples-718
title: "PR Insight: Ascend/samples #718"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - opencv
  - dependencies
  - cleanup
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/718"
---

# PR Insight: Ascend/samples #718

**Title:** 删除安装opencv_contrib

## Overview
This PR removes the installation of opencv_contrib from the samples repository, likely simplifying dependencies by using only the main OpenCV package or removing unused OpenCV extensions.

## Technical Significance
Removing opencv_contrib simplifies the dependency management and reduces installation complexity for samples. This focuses on the core OpenCV functionality that most samples require, reducing build time and potential version conflicts.

## Related
- N/A (dependency cleanup)