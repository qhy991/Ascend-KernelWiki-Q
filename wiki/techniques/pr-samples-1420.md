---
id: technique-pr-samples-1420
title: "PR Insight: Ascend/samples #1420"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolo
  - object-detection
  - multi-thread
  - venc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1420"
---

# PR Insight: Ascend/samples #1420

**Title:** 修改了 YOLOV3_coco_detection_multi_thread_VENC 中的queue.h和main.cpp

## Overview
This PR modifies the queue.h and main.cpp files in the YOLOv3 COCO multi-thread detection with VENC (Video Encoding) sample. The changes likely improve thread synchronization, queue management, or the overall multi-threaded pipeline.

## Technical Significance
Multi-threaded processing is essential for achieving real-time performance in video workflows. This sample shows how to properly implement multi-threading with YOLOv3 detection and video encoding on Ascend hardware.

## Related
- technique-multi-threading
- technique-yolo
- wiki-hardware-venc