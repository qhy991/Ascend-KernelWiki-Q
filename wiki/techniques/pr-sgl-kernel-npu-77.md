---
id: technique-pr-sgl-kernel-npu-77
title: "PR Insight: sgl-project/sgl-kernel-npu #77"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - batch-matmul
  - transpose
  - ascendc
  - testing
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/77"
---

# PR Insight: sgl-project/sgl-kernel-npu #77

**Title:** [feat] add batch_matmul_transpose op

## Overview
This PR adds a batch matrix multiplication with transpose operator optimized for Ascend NPUs. Includes comprehensive tiling logic (245 lines), kernel implementation (804 lines), and test validation. Precision testing passed on GSM8K dataset, confirming numerical correctness.

## Technical Significance
Provides optimized batch matmul with transpose for inference scenarios requiring weight transposition. The AscendC kernel implementation leverages hardware features for efficient batched matrix operations, critical for transformer attention mechanisms and other matmul-heavy inference workloads.

## Related
- technique-matmul
- technique-batch-operations
- technique-transpose-optimization
- technique-ascendc