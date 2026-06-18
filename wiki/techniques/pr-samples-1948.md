---
id: technique-pr-samples-1948
title: "PR Insight: Ascend/samples #1948"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - quantization
  - documentation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1948"
---

# PR Insight: Ascend/samples #1948

**Title:** update amct document path

## Overview
This PR updates the documentation path for AMCT (Ascend Model Compression Toolkit) within the samples repository. AMCT provides model quantization, pruning, and compression capabilities for deploying models on Ascend hardware, and the updated path reflects the current documentation structure after reorganization.

## Technical Significance
AMCT is essential for optimizing models to run efficiently on Ascend NPUs, particularly for quantization-aware training and post-training quantization workflows. Correct documentation paths ensure developers can access the right guides for using AMCT with frameworks like PyTorch, TensorFlow, and Caffe to achieve optimal accuracy and performance on Ascend910/910B.

## Related
- `technique-quantization`
- `pattern-model-compression`