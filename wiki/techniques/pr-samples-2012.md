---
id: technique-pr-samples-2012
title: "PR Insight: Ascend/samples #2012"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - refactoring
  - pytorch
  - mindspore
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2012"
---

# PR Insight: Ascend/samples #2012

**Title:** restruct amct pytorch & mindspore sample

## Overview
This PR restructures AMCT samples for PyTorch and MindSpore frameworks. The refactoring improves code organization and maintainability of model compression sample applications.

## Technical Significance
Well-structured sample code is easier for developers to understand and adapt. Restructuring AMCT samples clarifies how to apply compression techniques (quantization, pruning) across different frameworks, making it easier for developers to optimize their models for Ascend deployment.

## Related
- `technique-quantization-int8`