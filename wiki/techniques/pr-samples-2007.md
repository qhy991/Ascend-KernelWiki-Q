---
id: technique-pr-samples-2007
title: "PR Insight: Ascend/samples #2007"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - caffe
  - refactoring
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2007"
---

# PR Insight: Ascend/samples #2007

**Title:** restruct amct caffe sample

## Overview
This PR restructures the AMCT Caffe sample application. The refactoring improves code organization and maintainability of the model compression sample for Caffe models.

## Technical Significance
Restructuring AMCT samples clarifies how to apply compression techniques (quantization, pruning) to Caffe models. Well-organized sample code makes it easier for developers to adapt compression workflows for their own Caffe models deploying to Ascend hardware.

## Related
- `technique-quantization-int8`