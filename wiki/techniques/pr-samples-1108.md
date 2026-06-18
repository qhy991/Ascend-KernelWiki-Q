---
id: technique-pr-samples-1108
title: "PR Insight: Ascend/samples #1108"
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
  - "https://gitee.com/ascend/samples/pulls/1108"
---

# PR Insight: Ascend/samples #1108

**Title:** fix memory calculation mode in YUV400

## Overview
This PR fixes the memory calculation mode for YUV400 format. The correction changes how memory requirements are computed for YUV400 grayscale images, addressing calculation methodology issues.

## Technical Significance
The "mode" in memory calculation may refer to alignment requirements, stride calculations, or memory allocation strategies. Fixing the calculation mode ensures correct memory usage patterns that match hardware expectations for YUV400 processing on Ascend DVPP units.

## Related
- YUV400 format handling
- Memory calculation modes
- DVPP stride and alignment
- Grayscale image processing