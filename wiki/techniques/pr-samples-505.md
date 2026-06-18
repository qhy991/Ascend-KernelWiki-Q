---
id: technique-pr-samples-505
title: "PR Insight: Ascend/samples #505"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pytorch
  - onnx
  - model-conversion
  - samples
  - inception
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/505"
---

# PR Insight: Ascend/samples #505

**Title:** pytorch to onnx to om sample InceptionV3

## Overview
This PR adds a sample demonstrating the complete model conversion pipeline: PyTorch -> ONNX -> OM (Ascend Operator Model) for the InceptionV3 classification model.

## Technical Significance
Provides a complete example of the model conversion workflow, which is essential for deploying PyTorch models on Ascend hardware. The PyTorch->ONNX->OM chain is a standard deployment path for non-native frameworks.

## Related
- `pattern-model-conversion`
- `technique-inference-optimization`