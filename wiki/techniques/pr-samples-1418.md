---
id: technique-pr-samples-1418
title: "PR Insight: Ascend/samples #1418"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - imagenet
  - dynamic-batch
  - addition
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1418"
---

# PR Insight: Ascend/samples #1418

**Title:** add resnet50_imagenet_dynamic_dims

## Overview
This PR adds a ResNet50 ImageNet sample with dynamic dimensions support. The sample demonstrates how to handle variable input sizes when running ResNet50 inference on Ascend hardware.

## Technical Significance
Dynamic dimension support is important for flexible inference where input shapes are not fixed. This sample provides a reference for implementing dynamic input handling with ResNet50 on Ascend accelerators.

## Related
- technique-dynamic-shape
- technique-inference-optimization