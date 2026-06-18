---
id: technique-pr-samples-2001
title: "PR Insight: Ascend/samples #2001"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - onnx
  - refactoring
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2001"
---

# PR Insight: Ascend/samples #2001

**Title:** restruct amct_onnx sample

## Overview
This PR restructures the AMCT ONNX sample application. The refactoring improves code organization and maintainability of the model compression sample for ONNX models.

## Technical Significance
Restructuring AMCT samples clarifies how to apply compression techniques (quantization, pruning) to ONNX models. Well-organized sample code makes it easier for developers to adapt compression workflows for their own ONNX models deploying to Ascend hardware.

## Related
- `technique-quantization-int8`