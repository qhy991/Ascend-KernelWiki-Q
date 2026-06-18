---
id: technique-pr-samples-639
title: "PR Insight: Ascend/samples #639"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - qat
  - model-conversion
  - quantization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/639"
---

# PR Insight: Ascend/samples #639

**Title:** 添加convert QAT model用例

## Overview
This PR adds use cases for converting QAT (Quantization Aware Training) models to deployable quantized models. QAT is a technique where models are trained while simulating quantization effects to preserve accuracy.

## Technical Significance
QAT conversion is a critical step in deploying quantized models that maintain accuracy. Having sample code for this workflow enables users to apply QAT to their own models and deploy them efficiently on Ascend hardware with minimal accuracy loss.

## Related
- technique-operator-fusion
- Quantization Aware Training (QAT)
- Model conversion
- Post-training quantization