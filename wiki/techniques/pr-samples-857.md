---
id: technique-pr-samples-857
title: "PR Insight: Ascend/samples #857"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - image-classification
  - caffe
  - asynchronous-inference
  - pipeline
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/857"
---

# PR Insight: Ascend/samples #857

**Title:** 新增基于 Caffe ResNet-50 网络实现图片分类（异步推理）

## Overview
This PR adds a new sample implementing image classification using Caffe's ResNet-50 network with asynchronous inference. The sample demonstrates how to build efficient inference pipelines that overlap data preprocessing, model execution, and post-processing using async operations.

## Technical Significance
Asynchronous inference is essential for maximizing NPU throughput in production systems. This sample shows how to use Ascend's async API to pipeline operations, reducing overall latency by overlapping preprocessing, inference, and post-processing stages. It demonstrates advanced execution patterns for achieving high-performance inference on Ascend hardware, complementing the synchronous inference sample for comparison.

## Related
- Asynchronous inference patterns
- Pipeline optimization on Ascend
- ResNet-50 high-performance deployment
- Throughput optimization techniques
- Async API usage in CANN