---
id: technique-pr-samples-859
title: "PR Insight: Ascend/samples #859"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - image-classification
  - caffe
  - dvpp
  - synchronous-inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/859"
---

# PR Insight: Ascend/samples #859

**Title:** 新增基于Caffe ResNet-50网络实现图片分类（图片解码+缩放+同步推理）

## Overview
This PR adds a new sample implementing image classification using Caffe's ResNet-50 network. The sample includes image decoding, resizing, and synchronous inference, demonstrating an end-to-end image classification pipeline on Ascend NPU.

## Technical Significance
ResNet-50 is a widely used image classification model, and this sample provides a complete reference for deploying Caffe models on Ascend. The inclusion of DVPP-based image decoding and resizing shows how to leverage Ascend's hardware-accelerated preprocessing, while synchronous inference demonstrates the basic inference execution pattern. This is valuable for developers learning to deploy classic vision models on Ascend NPU.

## Related
- ResNet-50 inference on Ascend
- Caffe model deployment
- DVPP image preprocessing
- Synchronous inference patterns
- Image classification pipelines