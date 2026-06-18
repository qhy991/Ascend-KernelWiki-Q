---
id: technique-pr-samples-1811
title: "PR Insight: Ascend/samples #1811"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - resnet
  - rtsp
  - acllite
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1811"
---

# PR Insight: Ascend/samples #1811

**Title:** 【案例新增】 新增sampleResnetRtsp- PYAcllite版

## Overview
This PR adds a new Python-based sampleResnetRtsp implementation using the PYAcllite framework. It performs ResNet inference on RTSP video streams.

## Technical Significance
Adding Python ACL lite samples expands accessibility for developers who prefer Python over C++ for inference applications. The RTSP streaming pattern demonstrates real-time video inference, which is essential for surveillance, analytics, and live video processing use cases.

## Related
- `wiki-technique-inference`
- `wiki-technique-video-processing`
- `wiki-technique-acl`