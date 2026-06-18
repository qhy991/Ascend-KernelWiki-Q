---
id: technique-pr-samples-1914
title: "PR Insight: Ascend/samples #1914"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - onnx
  - plugin
  - custom-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1914"
---

# PR Insight: Ascend/samples #1914

**Title:** 添加onnx插件代码

## Overview
This PR adds ONNX plugin code to the samples repository, demonstrating how to extend ONNX model support with custom operators. The plugin code enables ONNX models with unsupported or custom operators to run on Ascend hardware by providing the necessary operator implementations and registration logic.

## Technical Significance
ONNX plugin support is crucial for deploying complex models that use non-standard operators. This sample shows how to bridge ONNX operators to AscendCL or AscendC implementations, enabling flexible model deployment on Ascend910/910B while maintaining ONNX's portability benefits across different inference frameworks.

## Related
- `pattern-onnx-import`
- `technique-custom-operator`