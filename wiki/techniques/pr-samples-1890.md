---
id: technique-pr-samples-1890
title: "PR Insight: Ascend/samples #1890"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - ascendc
  - kernel-launch
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1890"
---

# PR Insight: Ascend/samples #1890

**Title:** 添加MatMul调用样例

## Overview
This PR adds a sample demonstrating how to call the MatMul operator using direct kernel invocation methods, showing the API patterns for launching kernels from host code.

## Technical Significance
Provides a reference for kernel launching patterns, demonstrating how to set up input/output buffers, configure tiling parameters, and invoke AscendC kernels from application code.

## Related
- `kernel-matmul-ascendc`
- `technique-instruction-queue`