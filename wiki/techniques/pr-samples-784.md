---
id: technique-pr-samples-784
title: "PR Insight: Ascend/samples #784"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - video
  - vdec
  - venc
  - dvpp
  - testcase
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/784"
---

# PR Insight: Ascend/samples #784

**Title:** 修改vdecandvenc testcase

## Overview
This PR modifies the test case for VDEC (video decode) and VENC (video encode) operations. These DVPP (Digital Vision Pre-Processing) operations handle video decoding and encoding on Ascend hardware.

## Technical Significance
Video decode and encode are essential operations for video processing pipelines on Ascend. This test case modification likely improves test coverage, fixes test failures, or adds new test scenarios for DVPP video operations. Proper testing of VDEC and VENC is important for ensuring video processing reliability on Ascend NPU.

## Related
- DVPP video decoding (VDEC)
- DVPP video encoding (VENC)
- Video processing test cases
- DVPP API testing