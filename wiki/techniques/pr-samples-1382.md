---
id: technique-pr-samples-1382
title: "PR Insight: Ascend/samples #1382"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpeg-decoding
  - dvpp
  - exit-condition
  - device-runtime
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1382"
---

# PR Insight: Ascend/samples #1382

**Title:** 1. jpegd解码添加退出条件，待发送帧全部完成后退出； 2. 修改device不能运行问题

## Overview
This PR fixes two issues: 1) Adds an exit condition to JPEG decoding so the process exits after all pending frames are processed, and 2) fixes a problem where the device could not run. These improvements ensure proper shutdown and execution stability for DVPP JPEG decoding samples.

## Technical Significance
Proper frame processing lifecycle management is critical for video applications. The exit condition fix ensures clean shutdown, while the device runtime fix ensures samples can execute reliably on Ascend hardware.

## Related
- wiki-hardware-dvpp
- technique-video-processing
- technique-runtime-management