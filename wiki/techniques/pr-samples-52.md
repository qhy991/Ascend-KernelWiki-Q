---
id: technique-pr-samples-52
title: "PR Insight: Ascend/samples #52"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-op
  - tbe
  - tensorflow
  - caffe
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/52"
---

# PR Insight: Ascend/samples #52

**Title:** TBE custom operator sample of Caffe and TensorFlow for cann base

## Overview
This PR adds TBE (Tensor Boost Engine) custom operator samples for both Caffe and TensorFlow frameworks running on the CANN (Compute Architecture for Neural Networks) base platform. It provides baseline implementations demonstrating how to develop custom operators using TBE DSL/TIK interfaces.

## Technical Significance
Establishes foundational patterns for custom operator development on Ascend hardware, showing the integration points between TBE operators and deep learning frameworks. This serves as a reference implementation for developers porting custom operators to Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-cube-vector-overlap`