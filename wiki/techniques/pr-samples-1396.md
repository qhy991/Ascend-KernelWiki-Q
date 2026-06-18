---
id: technique-pr-samples-1396
title: "PR Insight: Ascend/samples #1396"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - code-refactoring
  - dvpp
  - vdec
  - venc
  - camera
  - yolo
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1396"
---

# PR Insight: Ascend/samples #1396

**Title:** 整改公共库+vdecandvenc+venc+根据地样例+新增camera样例+YOLOV3_coco_detection_video_DVPP_with_AIPP代码整改

## Overview
This PR performs comprehensive code refactoring across multiple areas: common libraries, VDEC and VENC samples, VENC base samples, adds a new camera sample, and refactors the YOLOv3 COCO video detection with DVPP and AIPP sample.

## Technical Significance
This large-scale refactoring improves code quality and consistency across video processing and object detection samples. It demonstrates best practices for DVPP video decode/encode workflows, camera integration, and YOLOv3 video detection with AIPP preprocessing on Ascend hardware.

## Related
- hw-dvpp
- hw-vdec
- hw-venc
- technique-yolo
- technique-video-processing