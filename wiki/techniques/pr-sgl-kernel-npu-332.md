---
id: technique-pr-sgl-kernel-npu-332
title: "PR Insight: sgl-project/sgl-kernel-npu #332"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - triangular-inverse
  - vector-unit
  - performance-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/332"
---

# PR Insight: sgl-project/sgl-kernel-npu #332

**Title:** Add AscendC triangular inverse

## Overview
This PR contributes an AscendC implementation of triangular matrix inverse using a column sweep algorithm on vector cores. The kernel supports fp16 and fp32 dtypes for matrix sizes 16, 32, 64, and 128, achieving approximately 1.78x geometric mean speedup over the reference Triton implementation. The kernel is integrated with the chunk_gated_delta_rule_native method and tested on Ascend A2 and 910B4.

## Technical Significance
The AscendC triangular inverse kernel provides significant performance improvements for linear attention operations by efficiently utilizing vector cores for column-wise matrix inversion. This optimization is particularly valuable for gated delta rule attention mechanisms used in models like Qwen, reducing computational overhead in the prefill phase.

## Related
- `kernel-matmul`, `kernel-triangular-inverse`, `hw-vector-unit`, `technique-operator-fusion`