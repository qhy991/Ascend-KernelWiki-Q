---
id: technique-pr-samples-853
title: "PR Insight: Ascend/samples #853"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - image-classification
  - caffe
  - synchronous-inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/853"
---

# PR Insight: Ascend/samples #853

**Title:** 基于 Caffe ResNet-50 网络实现图片分类（同步推理）

## Overview
This PR adds a new sample implementing image classification using Caffe's ResNet-50 network with synchronous inference. The sample demonstrates the basic pattern for running Caffe models on Ascend NPU with synchronous execution.

## Technical Significance
This sample provides a foundational reference for deploying Caffe models on Ascend. Synchronous inference is the simplest execution model, making it ideal for understanding the basic CANN API flow: model loading, input preparation, inference execution, and output retrieval. The ResNet-50 model is a standard benchmark for image classification, making this sample valuable for performance comparison and learning CANN development patterns.

## Related
- ResNet-50 inference basics
- Caffe model deployment on Ascend
- Synchronous inference API patterns
- Image classification workflows
- CANN model loading and execution