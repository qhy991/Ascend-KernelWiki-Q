---
id: technique-pr-samples-771
title: "PR Insight: Ascend/samples #771"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolo
  - object-detection
  - freetype
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/771"
---

# PR Insight: Ascend/samples #771

**Title:** YOLOV3_coco_detection_picture_with_freetype

## Overview
This PR adds or modifies a YOLOv3 COCO object detection sample that uses FreeType for text rendering in the output. The sample processes images to detect objects and renders results using FreeType font libraries.

## Technical Significance
Adding FreeType support to YOLOv3 samples enables high-quality text rendering for detection results, which is important for applications requiring annotated output with readable labels and confidence scores. This demonstrates integration of computer vision with text rendering on Ascend.

## Related
- N/A (YOLO detection sample)