---
id: technique-pr-samples-1803
title: "PR Insight: Ascend/samples #1803"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - amct
  - tensorflow
  - yolov3
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1803"
---

# PR Insight: Ascend/samples #1803

**Title:** change the model download path of yolov3 in amct_tensorflow

## Overview
This PR updates the model download path for YOLOv3 in the AMCT TensorFlow sample. AMCT is used for model quantization and compression.

## Technical Significance
Correct model download paths are essential for quantization samples to work reliably. YOLOv3 is a popular object detection model, and this sample demonstrates how to quantize TensorFlow models for deployment on Ascend hardware while maintaining accuracy.

## Related
- `wiki-technique-quantization`
- `wiki-technique-object-detection`