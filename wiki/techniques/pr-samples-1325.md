---
id: technique-pr-samples-1325
title: "PR Insight: Ascend/samples #1325"
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
  - "https://gitee.com/ascend/samples/pulls/1325"
---

# PR Insight: Ascend/samples #1325

**Title:** update cplusplus/level1_single_api/7_dvpp/venc_sample/src/sample_comm.h.

## Overview
This PR updates the sample_comm.h header file in the DVPP VENC sample. The changes improve common utilities and shared functionality for the video encoding sample.

## Technical Significance
Common header files like sample_comm.h provide reusable functions and structures across sample applications. Updates here improve consistency and reduce code duplication across DVPP samples.

## Related
- `technique-dvpp`
- `pattern-video-encoding`