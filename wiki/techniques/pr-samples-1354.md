---
id: technique-pr-samples-1354
title: "PR Insight: Ascend/samples #1354"
type: wiki-technique
architectures:
  - ascend310p
  - ascend910b
tags:
  - yolov3
  - object-detection
  - 310p
  - compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1354"
---

# PR Insight: Ascend/samples #1354

**Title:** YOLOV3_coco_detection_picture compatible 310P

## Overview
This PR makes the YOLOV3 COCO detection picture sample compatible with Ascend 310P. The changes adapt the model inference and preprocessing to work correctly on the 310P hardware.

## Technical Significance
Provides compatibility for a popular object detection model (YOLOv3) on the 310P variant, ensuring the sample works across different Ascend hardware generations. This involves adapting to any API differences or hardware-specific constraints of 310P.

## Related
- `kernel-yolov3`
- `pattern-object-detection`