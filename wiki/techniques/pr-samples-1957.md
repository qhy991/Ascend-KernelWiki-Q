---
id: technique-pr-samples-1957
title: "PR Insight: Ascend/samples #1957"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - venc
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1957"
---

# PR Insight: Ascend/samples #1957

**Title:** venc bug修复

## Overview
This PR fixes a bug in the video encoder (VENC) sample code within the samples repository. The VENC functionality demonstrates how to use Ascend's hardware-accelerated video encoding capabilities through the AscendCL API, and this fix corrects an issue that was preventing proper video encoding or causing runtime errors.

## Technical Significance
Video encoding is a key application scenario for Ascend NPUs, leveraging the dedicated VENC hardware unit. Bug fixes in sample code ensure developers have working reference implementations for video processing pipelines, which is particularly important for multimedia inference and transcoding workloads on Ascend910/910B.

## Related
- `hw-venc`
- `pattern-async-processing`