---
id: technique-pr-samples-598
title: "PR Insight: Ascend/samples #598"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - tensorflow
  - ascend
  - mobilenetv2
  - yolov3
  - quantization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/598"
---

# PR Insight: Ascend/samples #598

**Title:** 添加amct的sample，包括amct_tensorflow_ascend的mobilenetv2和yolov3

## Overview
This PR adds AMCT (Ascend Model Compression Toolkit) samples including amct_tensorflow_ascend examples for MobileNetV2 and YOLOv3 models. MobileNetV2 is a lightweight image classification model, while YOLOv3 is an object detection model.

## Technical Significance
Providing AMCT samples for both image classification (MobileNetV2) and object detection (YOLOv3) demonstrates quantization techniques across different model architectures and task types. This helps users understand how to apply AMCT effectively to their specific use cases.

## Related
- technique-operator-fusion
- AMCT toolkit
- TensorFlow quantization
- MobileNetV2
- YOLOv3
- Model compression