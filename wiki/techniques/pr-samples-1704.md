---
id: technique-pr-samples-1704
title: "PR Insight: Ascend/samples #1704"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - rtsp
  - video-streaming
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1704"
---

# PR Insight: Ascend/samples #1704

**Title:** 新增rtsp流样例sampleResnetRtsp

## Overview
This PR adds a new RTSP (Real-Time Streaming Protocol) sample featuring ResNet classification, demonstrating how to process video streams with real-time inference on Ascend hardware.

## Technical Significance
RTSP streaming inference is common in video surveillance, monitoring, and edge AI applications. This sample shows how to integrate video stream processing with ResNet classification on Ascend NPUs, handling the latency and throughput requirements of real-time inference.

## Related
- technique-video-streaming
- kernel-resnet