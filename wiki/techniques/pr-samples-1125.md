---
id: technique-pr-samples-1125
title: "PR Insight: Ascend/samples #1125"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yuv400
  - buffer-size
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1125"
---

# PR Insight: Ascend/samples #1125

**Title:** fix memory calculation  in YUV400

## Overview
This PR fixes memory calculation issues for YUV400 format. The correction ensures accurate memory allocation when processing YUV400 grayscale images in the DVPP pipeline.

## Technical Significance
YUV400 contains only the Y component, so memory calculation differs from multi-component formats like YUV420 or YUV422. Accurate calculation prevents buffer overruns (security risk) or under-allocation (data loss). This fix is important for grayscale image preprocessing workflows on Ascend NPU.

## Related
- YUV400 format handling
- Memory calculation patterns
- DVPP buffer allocation
- Grayscale image processing