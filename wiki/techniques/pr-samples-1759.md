---
id: technique-pr-samples-1759
title: "PR Insight: Ascend/samples #1759"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - amct
  - tensorflow
  - resnet
  - samples
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1759"
---

# PR Insight: Ascend/samples #1759

**Title:** 修改amct_tensorflow的resnet50_v1中模型名称的错误

## Overview
This PR fixes an error in the model name for ResNet50 v1 in the AMCT TensorFlow samples, ensuring correct model identification during quantization workflows.

## Technical Significance
Correct model names are essential for AMCT quantization processes, which rely on precise model identification to apply appropriate quantization strategies. Fixing naming errors prevents quantization failures and ensures accurate model conversion to INT8 or other quantized formats.

## Related
- `wiki-technique-quantization`
- `wiki-technique-model-conversion`