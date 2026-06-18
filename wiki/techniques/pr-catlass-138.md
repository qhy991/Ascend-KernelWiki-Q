---
id: technique-pr-catlass-138
title: "PR Insight: Ascend/catlass #138"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - shared-library
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/138"
---

# PR Insight: Ascend/catlass #138

**Title:** 共享库适配optimized_matmul优化-stable分支

## Overview
This PR adapts optimized_matmul for shared library usage on the stable branch. It brings production-ready shared library support to the stable catlass release.

## Technical Significance
Stable branch shared library support is critical for production deployments. This enables enterprise customers to integrate optimized matmul kernels without depending on development branch features.

## Related
- `kernel-matmul-ascendc`
- `technique-pipeline-scheduling`