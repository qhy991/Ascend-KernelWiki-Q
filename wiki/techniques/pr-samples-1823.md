---
id: technique-pr-samples-1823
title: "PR Insight: Ascend/samples #1823"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vdec
  - dvpp
  - samples
  - memory
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1823"
---

# PR Insight: Ascend/samples #1823

**Title:** 增加申请多个outbuf，支持多帧输入码流的解码

## Overview
This PR adds support for multiple output buffers in the VDEC (Video DECoder) sample, enabling the decoding of multi-frame input code streams.

## Technical Significance
Multi-buffer support is essential for efficient video decoding pipelines, allowing parallel processing of multiple frames and reducing decode latency. This pattern demonstrates proper buffer management for streaming video workloads on Ascend DVPP hardware.

## Related
- `hw-dvpp`
- `wiki-technique-pipeline-scheduling`
- `wiki-technique-video-processing`