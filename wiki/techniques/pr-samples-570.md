---
id: technique-pr-samples-570
title: "PR Insight: Ascend/samples #570"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - tensorflow
  - amct
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/570"
---

# PR Insight: Ascend/samples #570

**Title:** 添加amct_acl工具量化TensorFlow resnet50模型的使用示例

## Overview
This PR adds a usage example for quantizing TensorFlow ResNet50 models using the amct_acl tool. The example demonstrates how to apply the AMCT (Ascend Model Compression Toolkit) quantization pipeline to a common computer vision model for deployment on Ascend hardware.

## Technical Significance
Provides practical guidance for TensorFlow model quantization using AMCT's ACL interface, which is essential for deploying TensorFlow models on Ascend NPU hardware with optimized performance. The ResNet50 example serves as a template for quantizing other CNN models.

## Related
- `technique-quantization`
- `pattern-model-optimization`