---
id: technique-pr-samples-1185
title: "PR Insight: Ascend/samples #1185"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - new-sample
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1185"
---

# PR Insight: Ascend/samples #1185

**Title:** 新增resnet50_firstapp样例

## Overview
This PR adds a new resnet50_firstapp sample to the repository, likely as a first-application example for ResNet-50 inference.

## Technical Significance
ResNet-50 is a foundational CNN model widely used for image classification. This sample demonstrates how to optimize ResNet-50 inference on Ascend hardware, including efficient use of the cube unit for Conv2D operations, proper tiling strategies for feature maps, and memory management in the unified buffer to reduce data movement.

## Related
- kernel-matmul
- hw-cube-unit
- technique-tiling
- technique-nz-tiling