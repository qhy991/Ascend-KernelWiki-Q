---
id: technique-pr-sgl-kernel-npu-431
title: "PR Insight: sgl-project/sgl-kernel-npu #431"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rmsnorm
  - normalization
  - ltx-2
  - performance-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/431"
---

# PR Insight: sgl-project/sgl-kernel-npu #431

**Title:** add rmsnorm_without_weight kernel

## Overview
This PR adds a fused RMSNorm kernel implemented in Triton specifically for cases where learnable weights (gamma) are not required. The kernel is successfully integrated into the LTX-2 model pipeline, achieving approximately 3% improvement in E2E latency compared to the previous normalization implementation.

## Technical Significance
The weightless RMSNorm kernel provides optimized normalization for models that don't require learnable scale parameters, reducing computational overhead and memory access. The performance improvement demonstrates the value of specialized kernels for common normalization variants in transformer architectures.

## Related
- `kernel-rmsnorm`, `kernel-normalization`, `technique-operator-optimization`