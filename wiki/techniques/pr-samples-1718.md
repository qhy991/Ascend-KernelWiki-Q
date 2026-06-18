---
id: technique-pr-samples-1718
title: "PR Insight: Ascend/samples #1718"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - detect-and-classify
  - rtsp
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1718"
---

# PR Insight: Ascend/samples #1718

**Title:** 新增样例detect_and_classify  rtsp配置文件说明

## Overview
This PR adds RTSP (Real-Time Streaming Protocol) configuration file documentation for the detect_and_classify sample, explaining how to configure video stream inputs for combined detection and classification workflows.

## Technical Significance
RTSP is widely used for real-time video streaming in surveillance and monitoring applications. This sample demonstrates how to configure and process video streams for multi-task pipelines (object detection + classification) on Ascend hardware.

## Related
- technique-video-streaming
- technique-multi-task-inference