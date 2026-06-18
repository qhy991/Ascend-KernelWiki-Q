---
id: technique-pr-samples-770
title: "PR Insight: Ascend/samples #770"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-op
  - onnx
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/770"
---

# PR Insight: Ascend/samples #770

**Title:** add onnx custom op sample

## Overview
This PR adds custom operator samples specifically for ONNX framework integration, demonstrating how to register and execute custom operators within the ONNX Runtime on Ascend hardware.

## Technical Significance
Expands framework coverage to include ONNX, enabling developers to deploy custom operator kernels in ONNX-based inference pipelines and leverage ONNX's cross-platform capabilities with Ascend acceleration.

## Related
- `technique-operator-fusion`