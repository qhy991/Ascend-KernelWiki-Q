---
id: technique-pr-sgl-kernel-npu-152
title: "PR Insight: sgl-project/sgl-kernel-npu #152"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - build
  - cann
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/152"
---

# PR Insight: sgl-project/sgl-kernel-npu #152

**Title:** Add dependency on the moe header file of CANN

## Overview
This PR adds a build dependency on CANN's MoE header files to the kernel CMakeLists.txt, ensuring proper compilation of MoE operators that depend on CANN libraries.

## Technical Significance
Explicit dependency management ensures that MoE kernels compile correctly with the CANN toolkit version in use. This prevents linker errors and ABI mismatches that can occur when CANN APIs evolve across versions.

## Related
- `technique-moe`, `technique-cann`