---
id: technique-pr-samples-474
title: "PR Insight: Ascend/samples #474"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - yolo
  - coco
  - model-conversion
  - bugfix
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/474"
---

# PR Insight: Ascend/samples #474

**Title:** YOLOV4_coco_detection_car_picture&video的模型转换问题

## Overview
This PR addresses model conversion issues for YOLOv4 COCO detection models used in car picture and video samples, fixing problems that prevent proper model conversion to the OM format.

## Technical Significance
Resolves deployment blockers for YOLOv4 object detection samples, ensuring that COCO-trained models can be successfully converted and deployed on Ascend hardware. YOLOv4 is a widely used detection architecture.

## Related
- `pattern-model-conversion`
- `technique-inference-optimization`