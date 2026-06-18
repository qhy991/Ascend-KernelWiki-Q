---
id: technique-pr-samples-1999
title: "PR Insight: Ascend/samples #1999"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - tensorflow
  - refactoring
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1999"
---

# PR Insight: Ascend/samples #1999

**Title:** amct tensorflow sample restruct

## Overview
This PR restructures the AMCT TensorFlow sample application. The refactoring improves code organization and maintainability of the model compression sample for TensorFlow models.

## Technical Significance
Restructuring AMCT samples clarifies how to apply compression techniques (quantization, pruning) to TensorFlow models. Well-organized sample code makes it easier for developers to adapt compression workflows for their own TensorFlow models deploying to Ascend hardware.

## Related
- `technique-quantization-int8`