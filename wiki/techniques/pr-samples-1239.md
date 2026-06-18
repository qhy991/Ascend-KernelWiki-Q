---
id: technique-pr-samples-1239
title: "PR Insight: Ascend/samples #1239"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolo
  - onnx
  - model-conversion
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1239"
---

# PR Insight: Ascend/samples #1239

**Title:** use yolov3 onnx om

## Overview
This PR updates the YOLOv3 sample to use ONNX model format and convert to OM (Offline Model) format for Ascend inference.

## Technical Significance
Using ONNX models for YOLOv3 enables model portability from other frameworks to Ascend. The conversion to OM format is required for Ascend inference and involves operator mapping, constant folding, and graph optimizations. YOLOv3 is a computationally intensive object detection model that benefits from Ascend's cube unit for matrix operations in its backbone and detection head.

## Related
- kernel-matmul
- hw-cube-unit
- technique-operator-fusion