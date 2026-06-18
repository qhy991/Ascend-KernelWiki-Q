---
id: technique-pr-samples-680
title: "PR Insight: Ascend/samples #680"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - tensorflow
  - nuq
  - quantization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/680"
---

# PR Insight: Ascend/samples #680

**Title:** 添加Tensorflow NUQ用例

## Overview
This PR adds NUQ (Non-Uniform Quantization) use cases for TensorFlow models to the samples repository. NUQ is an advanced quantization technique that uses non-uniform quantization levels to better preserve model accuracy compared to standard uniform quantization.

## Technical Significance
Provides examples of NUQ implementation with TensorFlow models on Ascend hardware. NUQ is particularly valuable for models that are sensitive to quantization accuracy loss, offering better precision-performance trade-offs than standard 8-bit quantization.

## Related
- technique-operator-fusion
- Quantization techniques
- NUQ (Non-Uniform Quantization)