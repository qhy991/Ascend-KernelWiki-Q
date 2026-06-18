---
id: technique-pr-sgl-kernel-npu-384
title: "PR Insight: sgl-project/sgl-kernel-npu #384"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - cube-unit
  - matmul
  - performance-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/384"
---

# PR Insight: sgl-project/sgl-kernel-npu #384

**Title:** LoRA: Implementing kernels using CUBE computation unit

## Overview
This PR implements LoRA (Low-Rank Adaptation) kernels using the Ascend CUBE computation unit instead of VECTOR units for improved performance. The implementation includes sgemmc_expand, sgemmc_shrink kernels with comprehensive tiling and host-side support, targeting state update operations in Mamba-style models with LoRA adapters.

## Technical Significance
Utilizing the CUBE unit for LoRA operations provides significant performance improvements over vector-unit implementations by leveraging the dedicated matrix multiplication acceleration hardware. This optimization is particularly valuable for models with LoRA adapters applied to stateful operations like Mamba convolutions.

## Related
- `kernel-lora`, `kernel-sgemm`, `hw-cube-unit`, `technique-hardware-optimization`