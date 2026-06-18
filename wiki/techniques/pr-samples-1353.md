---
id: technique-pr-samples-1353
title: "PR Insight: Ascend/samples #1353"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - vdec
  - resize
  - dvpp
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1353"
---

# PR Insight: Ascend/samples #1353

**Title:** commit vdec&resize change

## Overview
This PR commits changes to the video decoding (VDEC) and resize functionality in the samples. The modifications improve how video frames are decoded and resized using DVPP.

## Technical Significance
Enhances the video processing pipeline by improving VDEC and resize operations. These are critical DVPP operations for handling video content efficiently on Ascend hardware, affecting both quality and performance.

## Related
- `technique-dvpp`
- `pattern-video-processing`