---
id: technique-pr-samples-1374
title: "PR Insight: Ascend/samples #1374"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - samples
  - yolo
  - object-detection
  - video
  - dvpp
  - aipp
  - porting
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1374"
---

# PR Insight: Ascend/samples #1374

**Title:** commit YOLOV3_coco_detection_video_DVPP_with_AIPP to 310P

## Overview
This PR ports the YOLOv3 COCO video detection sample with DVPP and AIPP to Ascend 310P. The porting involves adapting the sample for the 310P hardware architecture, potentially including memory and performance optimizations.

## Technical Significance
Porting samples to different Ascend architectures helps developers understand how to adapt code for different hardware variants. 310P is an edge inference device with different capabilities than 910B, making this sample valuable for edge AI development.

## Related
- technique-yolo
- hw-dvpp
- hw-aipp
- technique-hardware-adaptation