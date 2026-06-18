---
id: technique-pr-samples-1352
title: "PR Insight: Ascend/samples #1352"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - image-processing
  - logging
  - dvpp
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1352"
---

# PR Insight: Ascend/samples #1352

**Title:** 优化转换图片的log

## Overview
This PR optimizes the logging output during image conversion operations in the samples. The changes improve log clarity and reduce unnecessary output.

## Technical Significance
Better logging helps with debugging and understanding the image conversion pipeline. This is particularly useful for DVPP image processing samples where tracking format conversions and transformations is important.

## Related
- `technique-dvpp`
- `pattern-image-conversion`