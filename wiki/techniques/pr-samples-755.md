---
id: technique-pr-samples-755
title: "PR Insight: Ascend/samples #755"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolo
  - object-detection
  - video
  - multi-input
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/755"
---

# PR Insight: Ascend/samples #755

**Title:** 添加配置可选多路视频输入的yolov3目标检测样例

## Overview
This PR adds a YOLOv3 object detection sample with configurable multi-video input support. The sample allows users to configure and process multiple video streams simultaneously for object detection.

## Technical Significance
Adding configurable multi-video input capabilities to YOLOv3 samples enables batch processing of multiple video streams, which is important for real-world applications like surveillance and monitoring systems. This demonstrates how to handle concurrent video inputs efficiently on Ascend hardware.

## Related
- N/A (video batch processing)