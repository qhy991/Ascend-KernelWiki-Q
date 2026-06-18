---
id: technique-pr-samples-1698
title: "PR Insight: Ascend/samples #1698"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - vdec
  - rtsp
  - bugfix
  - video-decoding
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1698"
---

# PR Insight: Ascend/samples #1698

**Title:** rtsp流vdec解码bug修改

## Overview
This PR fixes a bug in the RTSP stream VDEC (Video Decoder) implementation, correcting issues that affected video decoding from real-time streaming protocols.

## Technical Significance
RTSP video decoding is critical for surveillance and monitoring applications. Bugs in VDEC can cause stream failures, frame drops, or memory leaks, compromising real-time inference reliability. This fix ensures stable video stream processing on Ascend hardware.

## Related
- technique-video-decoding
- technique-vdec