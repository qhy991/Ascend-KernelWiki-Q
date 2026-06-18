---
id: technique-pr-sgl-kernel-npu-92
title: "PR Insight: sgl-project/sgl-kernel-npu #92"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - matmul
  - operator-fusion
  - cube-unit
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/92"
---

# PR Insight: sgl-project/sgl-kernel-npu #92

**Title:** add FusedDeepMoe

## Overview
This PR adds a new FusedDeepMoe operator that integrates multiple operations into a single fused kernel for DeepSeek MoE inference. It includes host-side code, kernel implementations, tiling logic, and API bindings for the fused operator, along with extensive catlass library headers for matrix operations.

## Technical Significance
The FusedDeepMoe operator represents a major performance optimization for MoE inference by fusing dispatch, expert computation, and combine operations. This reduces memory access overhead and leverages Ascend's Cube unit for efficient grouped matrix multiplication. The catlass integration provides optimized GEMM kernels with multi-stage workspace and quantization support.

## Related
- `technique-operator-fusion`, `kernel-matmul-ascendc`, `technique-moe`