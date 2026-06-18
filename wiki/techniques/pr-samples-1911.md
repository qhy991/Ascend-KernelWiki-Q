---
id: technique-pr-samples-1911
title: "PR Insight: Ascend/samples #1911"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - ffmpeg
  - rtsp
  - acl
  - video
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1911"
---

# PR Insight: Ascend/samples #1911

**Title:** 修改C++ acllite中ffmpeg拉rtsp流传输协议设置参数

## Overview
This PR modifies the FFmpeg RTSP stream protocol parameters in the C++ ACLLite sample. ACLLite is a lightweight C++ wrapper around AscendCL, and this change updates how RTSP (Real-Time Streaming Protocol) video streams are pulled and configured for processing with FFmpeg before inference on Ascend hardware.

## Technical Significance
RTSP video streaming is a common input source for real-time inference applications like video analytics. Proper FFmpeg and RTSP parameter configuration ensures reliable video capture and frame extraction, which is critical for maintaining low-latency, high-throughput inference pipelines on Ascend910/910B for video analysis workloads.

## Related
- `pattern-video-pipeline`
- `technique-input-preprocessing`