---
id: technique-pr-samples-1642
title: "PR Insight: Ascend/samples #1642"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - aipp
  - preprocessing
  - code-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1642"
---

# PR Insight: Ascend/samples #1642

**Title:** sampleResnetAipp.cpp修改

## Overview
This PR modifies the sampleResnetAipp.cpp implementation, updating or improving the ResNet sample that uses AIPP (AI Preprocessing) for on-device image preprocessing.

## Technical Significance
AIPP enables hardware-accelerated preprocessing (resizing, normalization, color conversion) on Ascend devices, reducing data transfer overhead. This sample demonstrates how to integrate AIPP with ResNet inference for end-to-end optimized image classification pipelines.

## Related
- kernel-resnet
- technique-aipp