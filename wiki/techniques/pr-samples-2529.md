---
id: technique-pr-samples-2529
title: "PR Insight: Ascend/samples #2529"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - add
  - cpp-extension
  - custom-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2529"
---

# PR Insight: Ascend/samples #2529

**Title:** 新增add算子使用cppextension的方式调用

## Overview
This PR adds a sample demonstrating how to call the Add operator using cppextension. The example shows how to use C++ extensions for custom operator integration with PyTorch or other frameworks on Ascend hardware.

## Technical Significance
C++ extensions provide a way to implement custom operators with low-level control over NPU execution. Understanding cppextension usage is important for developers implementing domain-specific optimizations.

## Related
- `kernel-elementwise-ascendc`
- `hw-vector-unit`
- `technique-operator-fusion`