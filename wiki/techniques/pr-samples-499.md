---
id: technique-pr-samples-499
title: "PR Insight: Ascend/samples #499"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - resize
  - crop
  - computer-vision
  - bugfix
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/499"
---

# PR Insight: Ascend/samples #499

**Title:** 将resize为cropandpaste，修复框编左的问题

## Overview
This PR changes a resize operation to crop-and-paste to fix a box shifting issue (框编左的问题) in image processing samples. The fix corrects the positioning problem in the image transformation pipeline.

## Technical Significance
Resolves a specific image processing bug where bounding boxes or regions were incorrectly positioned after resize operations. The crop-and-paste approach provides more precise control over image regions.

## Related
- `technique-dvpp-optimization`
- `pattern-image-transform`