---
id: technique-pr-samples-642
title: "PR Insight: Ascend/samples #642"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - caffe
  - tensorflow
  - tensor-decompose
  - quantization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/642"
---

# PR Insight: Ascend/samples #642

**Title:** 添加AMCT Caffe张量分解样例和AMCT Tensorflow张量分解样例

## Overview
This PR adds AMCT tensor decomposition samples for both Caffe and TensorFlow frameworks. Tensor decomposition is a model compression technique that factorizes large weight tensors into smaller components to reduce memory and computational requirements.

## Technical Significance
Providing tensor decomposition samples across multiple frameworks (Caffe and TensorFlow) gives users comprehensive reference implementations for this optimization technique. Tensor decomposition is especially valuable for large transformer models where weight matrices can be factorized for efficiency.

## Related
- technique-operator-fusion
- Tensor decomposition
- Model compression
- Multi-framework support