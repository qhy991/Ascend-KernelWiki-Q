---
id: technique-pr-samples-1436
title: "PR Insight: Ascend/samples #1436"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - imagenet
  - dynamic-batch
  - model-update
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1436"
---

# PR Insight: Ascend/samples #1436

**Title:** resnet50_imagenet_dynamic_dims replace model

## Overview
This PR replaces the model in the ResNet50 ImageNet dynamic dimensions sample. The update likely provides a better or more up-to-date model file for testing dynamic input dimensions on Ascend hardware.

## Technical Significance
Dynamic dimension support is important for flexible inference scenarios where input sizes vary. This sample demonstrates how to handle variable input shapes with ResNet50 on Ascend accelerators.

## Related
- technique-dynamic-shape
- technique-inference-optimization