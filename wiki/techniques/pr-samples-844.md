---
id: technique-pr-samples-844
title: "PR Insight: Ascend/samples #844"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - video
  - h264
  - h265
  - bugfix
  - codec
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/844"
---

# PR Insight: Ascend/samples #844

**Title:** 更新video.py 修复h264被设置成h265的问题

## Overview
This PR updates video.py to fix a bug where the H.264 codec was incorrectly being set as H.265. The fix ensures the correct video codec configuration is used during video processing.

## Technical Significance
Codec configuration errors can cause video decoding/encoding failures or incorrect output. This fix addresses a critical bug in video processing pipelines, ensuring that H.264 video streams are handled correctly with the appropriate codec settings. This is important for video inference samples that use DVPP or other video processing capabilities on Ascend NPU.

## Related
- Video codec configuration on Ascend
- H.264/H.265 video processing
- DVPP video decoding
- Video preprocessing pipelines