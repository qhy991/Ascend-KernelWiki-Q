---
id: technique-pr-mindspeed-1970
title: "PR Insight: Ascend/MindSpeed #1970"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - build
  - pytorch
  - compilation
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1970"
---

# PR Insight: Ascend/MindSpeed #1970

**Title:** remove custom cxx_abi arg

## Overview
This PR removes a custom C++ ABI argument from the build configuration. The change likely resolves compatibility issues with different compiler environments or standard library configurations.

## Technical Significance
C++ ABI compatibility is crucial for linking with PyTorch and torch_npu libraries. Removing custom ABI arguments helps avoid binary compatibility issues and ensures proper linking with standard PyTorch builds on Ascend systems.

## Related
- build-system patterns
- pytorch-integration