---
id: technique-pr-sgl-kernel-npu-102
title: "PR Insight: sgl-project/sgl-kernel-npu #102"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - matmul
  - quantization
  - cube-unit
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/102"
---

# PR Insight: sgl-project/sgl-kernel-npu #102

**Title:** fix some bug for fused moe

## Overview
This PR fixes bugs in the FusedDeepMoe operator, affecting tiling code, kernel headers, and grouped matrix multiplication kernels. The fixes address issues in the MoE distribute/combine dispatch logic and per-token dequantization kernels.

## Technical Significance
Bug fixes in fused MoE operations are critical as errors can propagate through the entire expert routing and computation pipeline. The fixes likely address tiling boundary conditions, quantization correctness, or buffer management issues in the multi-stage workspace kernels.

## Related
- `technique-moe`, `kernel-matmul-ascendc`, `technique-quantization`