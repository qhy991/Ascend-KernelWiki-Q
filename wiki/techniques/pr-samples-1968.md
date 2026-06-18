---
id: technique-pr-samples-1968
title: "PR Insight: Ascend/samples #1968"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kernel-launch
  - pybind
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1968"
---

# PR Insight: Ascend/samples #1968

**Title:** 新增pybind调用Kernel launch样例

## Overview
This PR adds a sample demonstrating how to invoke AscendC kernels from Python using pybind11, enabling seamless integration of custom kernels with Python-based deep learning frameworks and applications.

## Technical Significance
Provides a Python bridge for AscendC kernel development, allowing developers to use familiar Python tooling while still leveraging optimized custom kernels. This is essential for rapid prototyping and integration with PyTorch/TensorFlow.

## Related
- `technique-instruction-queue`
- `kernel-matmul-ascendc`