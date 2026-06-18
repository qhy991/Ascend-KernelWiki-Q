---
id: technique-pr-samples-1936
title: "PR Insight: Ascend/samples #1936"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - pybind
  - ascendc
  - custom-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1936"
---

# PR Insight: Ascend/samples #1936

**Title:** 添加pybind调用Ascend C算子样例

## Overview
This PR adds a sample demonstrating how to use pybind to invoke AscendC operators from Python code. The sample shows the integration pattern for binding custom AscendC kernels as Python-callable functions, enabling Python applications to leverage high-performance NPU kernels while maintaining Python-level convenience.

## Technical Significance
PyBind integration is essential for making AscendC operators accessible from Python ML frameworks like PyTorch and TensorFlow. This sample provides reference code for the C++/Python boundary, demonstrating how to pass tensors between Python and AscendC kernels, handle data conversions, and manage memory across the interface on Ascend910/910B.

## Related
- `technique-custom-operator`
- `pattern-python-interop`