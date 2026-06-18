---
id: technique-pr-samples-1692
title: "PR Insight: Ascend/samples #1692"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - atc
  - model-conversion
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1692"
---

# PR Insight: Ascend/samples #1692

**Title:** 新增atc sample

## Overview
This PR adds a new ATC (Ascend Tensor Compiler) sample to the repository, providing an example of model conversion to Ascend's OM format.

## Technical Significance
ATC is the core compiler for converting models (from frameworks like TensorFlow, PyTorch, ONNX) to Ascend's optimized format. Having clear ATC samples helps developers understand the conversion workflow, including input specifications, optimization settings, and handling of model inputs/outputs.

## Related
- technique-atc-compiler