---
id: technique-pr-samples-1971
title: "PR Insight: Ascend/samples #1971"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - matmul
  - multi-architecture
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1971"
---

# PR Insight: Ascend/samples #1971

**Title:** 修改MatMul单算子调用用例，增加310p支持

## Overview
This PR modifies the MatMul single operator invocation sample to support Ascend310P architecture, adding platform-specific adaptations for this edge computing variant.

## Technical Significance
Extends MatMul sample coverage to include edge computing platforms, showing how to adapt matrix multiplication kernels for different hardware capabilities and memory configurations.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`