---
id: technique-pr-samples-633
title: "PR Insight: Ascend/samples #633"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - tensorflow
  - resnet
  - retrain
  - quantization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/633"
---

# PR Insight: Ascend/samples #633

**Title:** 提交AMCT-TF ResNet-50 retrain样例

## Overview
This PR adds an AMCT TensorFlow ResNet-50 retrain sample, demonstrating the workflow for retraining a quantized ResNet-50 model to recover accuracy lost during quantization. ResNet-50 is a widely used image classification model.

## Technical Significance
ResNet-50 is a standard benchmark for quantization accuracy studies. Having a reference implementation for the retrain workflow helps users understand how to fine-tune quantized models effectively, which is crucial for maintaining accuracy in production deployments.

## Related
- technique-operator-fusion
- Quantization retraining
- ResNet-50
- Image classification
- AMCT TensorFlow