---
id: technique-pr-samples-1507
title: "PR Insight: Ascend/samples #1507"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - numba
  - migration
  - tbe-tik
  - blast
  - university-contribution
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1507"
---

# PR Insight: Ascend/samples #1507

**Title:** 西工大-CANN Numba 应用迁移案例-TIK_BLAST算子

## Overview
This PR adds a CANN Numba application migration case contributed by Northwestern Polytechnical University, focusing on the TIK_BLAST operator. Numba is a Python JIT compiler for numerical code.

## Technical Significance
Migrating Numba-optimized Python code to Ascend CANN demonstrates cross-platform performance optimization patterns. The TIK_BLAST operator is likely a high-performance BLAS implementation using TIK (Tensor Inference Kernel). This sample shows how to translate Python-based numerical kernels to AscendC/TIK for NPU acceleration.

## Related
- `technique-migration`
- `technique-numba-to-ascendc`
- `technique-tik`
- `kernel-blas`
- `kernel-matmul`