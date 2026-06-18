---
id: technique-pr-sgl-kernel-npu-339
title: "PR Insight: sgl-project/sgl-kernel-npu #339"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - test
  - triangular-inverse
  - verification
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/339"
---

# PR Insight: sgl-project/sgl-kernel-npu #339

**Title:** (test) add solve_tril from upstream

## Overview
This PR adds a unit test for the solve_tril function from the flash-linear-attention upstream repository. The test validates triangular matrix solving functionality against NumPy's column sweep reference implementation across various batch sizes, sequence lengths, head dimensions, and chunk sizes.

## Technical Significance
Adding comprehensive tests for triangular matrix operations ensures correctness and numerical accuracy of linear attention kernels. The test coverage across different configurations helps validate the robustness of the implementation and detect numerical instabilities across various model shapes and data types.

## Related
- `kernel-triangular-inverse`, `kernel-solve-tril`, `technique-testing`