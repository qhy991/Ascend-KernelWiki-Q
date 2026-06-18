---
id: technique-pr-samples-790
title: "PR Insight: Ascend/samples #790"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - tensorflow
  - mobilenetv2
  - quantization
  - compression
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/790"
---

# PR Insight: Ascend/samples #790

**Title:** amct_tf_ascend mobilenetv2模型变为tf官方模型

## Overview
This PR updates the AMCT TensorFlow Ascend sample to use the official TensorFlow MobileNetV2 model instead of a custom version. AMCT is Ascend's Model Compression Toolkit.

## Technical Significance
Using the official TensorFlow MobileNetV2 model improves sample consistency and reproducibility. MobileNetV2 is a widely-used efficient model for mobile inference, and this sample demonstrates how to apply AMCT compression techniques to official TensorFlow models for deployment on Ascend. This provides a more standard and reference-worthy example of model compression workflows.

## Related
- AMCT TensorFlow model compression
- MobileNetV2 quantization and compression
- Official TensorFlow model deployment
- Model compression workflows for Ascend