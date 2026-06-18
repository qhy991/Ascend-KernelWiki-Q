---
id: technique-pr-samples-557
title: "PR Insight: Ascend/samples #557"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - amct
  - caffe
  - mindspore
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/557"
---

# PR Insight: Ascend/samples #557

**Title:** amct caffe faster-rcnn and amct_mindspore resnet50 sample

## Overview
This PR adds AMCT quantization samples for Caffe's Faster R-CNN object detection model and MindSpore's ResNet50 classification model. These examples expand the quantization toolkit coverage to multiple frameworks (Caffe and MindSpore) and model types (detection and classification).

## Technical Significance
Demonstrates AMCT's cross-framework quantization capabilities, showing how to optimize both object detection (Faster R-CNN) and image classification (ResNet50) models. This is important for developers working with different ML frameworks on Ascend hardware.

## Related
- `technique-quantization`
- `kernel-matmul`
- `pattern-model-optimization`