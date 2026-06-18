---
id: technique-pr-samples-1734
title: "PR Insight: Ascend/samples #1734"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - vdec
  - device-id
  - video-decoding
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1734"
---

# PR Insight: Ascend/samples #1734

**Title:** vdec sample 支持设置 device id

## Overview
This PR adds device ID configuration support to the VDEC (Video Decoder) sample, allowing users to specify which Ascend device to use for video decoding operations.

## Technical Significance
Multi-device scenarios are common in production environments. The ability to select specific device IDs enables load balancing across multiple NPUs and prevents resource conflicts in systems with multiple Ascend cards.

## Related
- technique-multi-device
- technique-video-decoding