---
id: technique-pr-samples-1210
title: "PR Insight: Ascend/samples #1210"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - mindspore
  - model-inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1210"
---

# PR Insight: Ascend/samples #1210

**Title:** add mindspore model to infer app examples.

## Overview
This PR adds MindSpore model examples to the inference application samples.

## Technical Significance
Adding MindSpore model support expands the framework compatibility of Ascend samples. MindSpore is Huawei's deep learning framework, and its models may have specific operator patterns and optimization requirements when running on Ascend hardware. This includes efficient use of the cube unit for matrix operations and proper memory tiling strategies.

## Related
- kernel-matmul
- hw-cube-unit
- technique-tiling