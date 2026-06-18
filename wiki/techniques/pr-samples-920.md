---
id: technique-pr-samples-920
title: "PR Insight: Ascend/samples #920"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dvpp
  - video
  - preprocessing
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/920"
---

# PR Insight: Ascend/samples #920

**Title:** dvpp sample first submit

## Overview
This PR is the first submission of a DVPP (Digital Vision Pre-Processing) sample. DVPP is Ascend's hardware-accelerated image and video preprocessing module, providing efficient decoding, resizing, and format conversion on the NPU.

## Technical Significance
DVPP samples are crucial for understanding how to leverage Ascend's dedicated video processing hardware. This sample demonstrates the DVPP API usage pattern, showing how to offload video decoding, JPEG encoding/decoding, and image preprocessing operations to the DVPP hardware instead of using CPU-based libraries. This is essential for building end-to-end inference pipelines with maximum throughput.

## Related
- DVPP hardware acceleration for video processing
- Image preprocessing pipelines on NPU
- DVPP API usage patterns
- Video inference workflows