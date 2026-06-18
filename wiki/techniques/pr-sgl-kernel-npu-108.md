---
id: technique-pr-sgl-kernel-npu-108
title: "PR Insight: sgl-project/sgl-kernel-npu #108"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - matmul
  - operator-fusion
  - quantization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/108"
---

# PR Insight: sgl-project/sgl-kernel-npu #108

**Title:** Synchronous fusion moe

## Overview
This PR implements synchronous fusion for MoE operations and adds top9 expert selection support. It updates tiling logic, kernel headers, and adds new activation and GEMM kernels for the fused MoE implementation.

## Technical Significance
Synchronous fusion ensures all MoE stages complete together, reducing synchronization overhead and enabling better pipeline efficiency. The top9 support expands routing flexibility beyond typical top8, improving model accuracy at the cost of additional computation. The catlass integration provides optimized kernels for the fused pipeline.

## Related
- `technique-operator-fusion`, `technique-moe`, `kernel-matmul-ascendc`