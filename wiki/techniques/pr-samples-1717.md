---
id: technique-pr-samples-1717
title: "PR Insight: Ascend/samples #1717"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct-tf
  - quantization
  - resnet
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1717"
---

# PR Insight: Ascend/samples #1717

**Title:** 【DTS2023041914889】amct_tf resnet模型路径失效

## Overview
This PR fixes a bug where the ResNet model path was invalid in the AMCT (Ascend Model Compression Toolkit) TensorFlow sample (amct_tf), addressing issue DTS2023041914889.

## Technical Significance
AMCT is used for model quantization and compression before Ascend deployment. Path resolution bugs can prevent samples from running, blocking developers from learning quantization workflows. This fix ensures quantization examples work correctly.

## Related
- technique-quantization
- technique-amct