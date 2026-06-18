---
id: technique-pr-samples-1004
title: "PR Insight: Ascend/samples #1004"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - tensorflow
  - resnet
  - quantization
  - pruning
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1004"
---

# PR Insight: Ascend/samples #1004

**Title:** 提交AMCT-TF ResNet-50 稀疏及混合量化样例

## Overview
Adds AMCT TensorFlow samples for ResNet-50 demonstrating sparsity (pruning) and mixed quantization techniques.

## Technical Significance
Provides comprehensive examples for two key compression techniques: structured sparsity for inference acceleration and mixed quantization for accuracy-speed tradeoffs. Both techniques map to hardware features on Ascend.

## Related
- `technique-quantization` / `technique-pruning` / `kernel-resnet`
