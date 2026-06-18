---
id: technique-pr-samples-1498
title: "PR Insight: Ascend/samples #1498"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolov4
  - object-detection
  - output-management
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1498"
---

# PR Insight: Ascend/samples #1498

**Title:** samples/cplusplus/level2_simple_inference/2_object_detection/YOLOV4_coco_detection_picture输出目录修改

## Overview
This PR modifies the output directory for the YOLOV4 COCO object detection sample. YOLOV4 is an evolution of the YOLO object detection architecture.

## Technical Significance
Output directory management affects sample usability and integration with downstream processing pipelines. Changes may standardize output paths, fix permission issues, or improve organization of detection results (bounding boxes, confidence scores, class labels).

## Related
- `kernel-yolo`
- `technique-object-detection`
- `technique-io-management`
- `technique-file-path-handling`