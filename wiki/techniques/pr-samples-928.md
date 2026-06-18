---
id: technique-pr-samples-928
title: "PR Insight: Ascend/samples #928"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - onnx
  - col2im
  - feature-add
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/928"
---

# PR Insight: Ascend/samples #928

**Title:** 【onnx】add col2im adapt

## Overview
Adds col2im (column-to-image) adaptation for ONNX model samples, which is the inverse operation of im2col commonly used in CNN backpropagation.

## Technical Significance
Col2im is needed for certain CNN operators during inference or model conversion. Adding this support expands ONNX model compatibility on Ascend, enabling deployment of more diverse architectures.

## Related
- `kernel-cnn` / `technique-onnx-conversion`
