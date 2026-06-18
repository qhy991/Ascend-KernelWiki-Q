---
id: technique-pr-catlass-135
title: "PR Insight: Ascend/catlass #135"
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
  - "https://gitee.com/ascend/catlass/pulls/135"
---

# PR Insight: Ascend/catlass #135

**Title:** 共享库适配optimized_matmul优化

## Overview
This PR adapts the optimized_matmul implementation for shared library usage. It ensures that optimized matmul kernels can be properly packaged and loaded from a shared library on Ascend systems.

## Technical Significance
Shared library support enables catlass to be integrated into larger applications without recompilation. This is essential for production deployment where matmul kernels need to be versioned and distributed independently from the main application.

## Related
- `kernel-matmul-ascendc`
- `technique-pipeline-scheduling`