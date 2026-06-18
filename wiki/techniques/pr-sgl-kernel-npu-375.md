---
id: technique-pr-sgl-kernel-npu-375
title: "PR Insight: sgl-project/sgl-kernel-npu #375"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - elementwise
  - rmsnorm
  - mul-add
  - normalization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/375"
---

# PR Insight: sgl-project/sgl-kernel-npu #375

**Title:** Add rmsnorm_bias and mul_add ops

## Overview
This PR adds two new elementwise operators: rmsnorm_bias (Root Mean Square Layer Normalization with bias) and mul_add (multiply-add fusion). The implementations are integrated into the NPU kernel library and optimized for Ascend hardware, with the rmsnorm_bias operator also being applied to split_qkv_rmsnorm_rope operations.

## Technical Significance
Adding specialized normalization and arithmetic operators expands the NPU operator library, enabling more efficient fused operations for common transformer layer patterns. The rmsnorm_bias operator supports models requiring bias terms in normalization, while mul_add provides efficient multiply-add fusion for elementwise computations.

## Related
- `kernel-rmsnorm`, `kernel-mul-add`, `kernel-elementwise`, `technique-operator-fusion`