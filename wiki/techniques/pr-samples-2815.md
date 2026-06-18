---
id: technique-pr-samples-2815
title: "PR Insight: Ascend/samples #2815"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pybind
  - custom-operator
  - pytorch
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2815"
---

# PR Insight: Ascend/samples #2815

**Title:** Add examples for PyTorch custom operator invocation using Pybind and torch.library

## Overview
This PR adds examples demonstrating how to invoke PyTorch custom operators using PyBind11 and the torch.library API. The samples show the complete workflow from AscendC kernel implementation to PyTorch integration.

## Technical Significance
This integration is crucial for production deployment of custom AscendC operators. The torch.library API provides a clean interface for registering custom operators, while PyBind11 enables efficient Python-C++ interop. These examples give developers a complete reference for accelerating PyTorch models with custom Ascend kernels.

## Related
- technique-operator-fusion
- pr-samples-2776