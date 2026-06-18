---
id: technique-pr-samples-1286
title: "PR Insight: Ascend/samples #1286"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - opencv
  - image-preprocessing
  - samples
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1286"
---

# PR Insight: Ascend/samples #1286

**Title:** 添加opencv处理图片的预处理方式

## Overview
This PR adds OpenCV-based image preprocessing methods to a sample. The changes provide alternative image processing options using the popular OpenCV library.

## Technical Significance
OpenCV is widely used for image preprocessing. Adding OpenCV support gives developers flexibility to choose between OpenCV and DVPP for image operations, which is useful for different use cases and portability.

## Related
- `technique-dvpp`
- `pattern-image-preprocessing`