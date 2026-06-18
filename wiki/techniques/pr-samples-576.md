---
id: technique-pr-samples-576
title: "PR Insight: Ascend/samples #576"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - acl
  - onnx
  - resnet101
  - quantization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/576"
---

# PR Insight: Ascend/samples #576

**Title:** 添加amct_acl工具量化onnx resnet101模型的使用示例

## Overview
This PR adds an example demonstrating how to use the AMCT ACL tool to quantize an ONNX ResNet-101 model. ResNet-101 is a deep residual network for image classification, and this sample shows the full quantization workflow.

## Technical Significance
ONNX is a widely used model exchange format, and ResNet-101 is a standard benchmark for deep learning performance. This sample demonstrates how to bring ONNX models to Ascend with quantization, which is critical for production deployment of pre-trained models.

## Related
- technique-operator-fusion
- AMCT ACL
- ONNX quantization
- ResNet-101
- Model conversion
- Production deployment