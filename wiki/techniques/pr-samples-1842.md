---
id: technique-pr-samples-1842
title: "PR Insight: Ascend/samples #1842"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - resnet
  - rtsp
  - inference
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1842"
---

# PR Insight: Ascend/samples #1842

**Title:** sampleResNetRtsp cpp代码目录调整

## Overview
This PR reorganizes the C++ code directory structure for the sampleResNetRtsp sample, which performs ResNet inference on RTSP video streams.

## Technical Significance
Proper code organization improves maintainability and makes samples easier to understand. The ResNet RTSP sample demonstrates real-time video inference using the Ascend ACL (Ascend Computing Language) framework, showing how to process streaming video inputs efficiently on Ascend hardware.

## Related
- `wiki-technique-inference`
- `wiki-technique-video-processing`