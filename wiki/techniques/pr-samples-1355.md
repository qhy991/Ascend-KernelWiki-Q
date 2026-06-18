---
id: technique-pr-samples-1355
title: "PR Insight: Ascend/samples #1355"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - dvpp
  - venc
  - samples
  - cplusplus
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1355"
---

# PR Insight: Ascend/samples #1355

**Title:** update cplusplus/level1_single_api/7_dvpp/venc_sample/src/sample_looper.cpp.

## Overview
This PR updates the sample_looper.cpp file in the DVPP VENC sample. The changes improve the video encoding sample implementation, focusing on the looper logic that handles the encoding pipeline.

## Technical Significance
Enhances the DVPP (Digital Vision Pre-Processing) video encoding sample, which demonstrates how to use the VENC (Video Encoding) capabilities of Ascend NPUs. The looper logic is critical for proper frame processing and encoding throughput.

## Related
- `technique-dvpp`
- `pattern-video-encoding`