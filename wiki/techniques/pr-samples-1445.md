---
id: technique-pr-samples-1445
title: "PR Insight: Ascend/samples #1445"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolo
  - object-detection
  - dvpp
  - aipp
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1445"
---

# PR Insight: Ascend/samples #1445

**Title:** 【轻量级 PR】：add cplusplus/level2/2_object_detection/YOLOV3_coco_detection_picture_DVPP_with_AIPP/data/.keep.

## Overview
This is a lightweight PR adding a .keep file to the data directory of the YOLOv3 COCO detection sample that uses DVPP with AIPP. The .keep file ensures the directory is preserved in version control even when empty.

## Technical Significance
Maintaining directory structure with .keep files helps preserve the expected sample layout, ensuring developers can run samples without missing directories.

## Related
- samples-object-detection
- technique-yolo
- hw-dvpp