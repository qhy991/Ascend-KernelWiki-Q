---
id: technique-pr-samples-1189
title: "PR Insight: Ascend/samples #1189"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - code-reorganization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1189"
---

# PR Insight: Ascend/samples #1189

**Title:** 更换resnet50_firstapp样例目录结构

## Overview
This PR reorganizes the directory structure of the resnet50_firstapp sample application.

## Technical Significance
Directory reorganization improves code discoverability and maintainability. For ResNet-50 inference samples, this may involve separating model loading, preprocessing, inference, and postprocessing code into clearer modules. ResNet-50 is a CNN that heavily relies on Conv2D and matrix multiplication operations optimized by Ascend's cube unit.

## Related
- kernel-matmul
- wiki-hardware-cube-unit
- technique-operator-fusion