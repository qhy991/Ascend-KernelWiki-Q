---
id: technique-pr-sgl-kernel-npu-154
title: "PR Insight: sgl-project/sgl-kernel-npu #154"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - layernorm
  - flash-attention
  - triton
  - vector-unit
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/154"
---

# PR Insight: sgl-project/sgl-kernel-npu #154

**Title:** [Kernel] add Flash-Linear-Attention/layernorm_gated Triton op

## Overview
This PR adds a gated LayerNorm Triton operator for Flash-Linear-Attention (FLA) on NPU. The implementation provides two kernel variants: a SIMD version (`_layer_norm_fwd_1pass_kernel_npu_simd`) and a batched version (`_layer_norm_fwd_1pass_kernel_npu`), both adapted from SGLang's original implementation. The operator supports optional bias, gated activation via a secondary input Z, RMSNorm variants, and configurable group sizes. The PR also adds a utility function `get_device_properties()` to query NPU AI core and vector core counts for grid sizing.

## Technical Significance
The gated LayerNorm is a critical component in Flash-Linear-Attention architectures, where normalization is applied either before or after gating (elementwise multiplication with sigmoid(Z)). The kernels leverage NPU vector cores with optimized tiling (BLOCK_M=48 rows, BLOCK_N adapted to feature dimension) and use `get_device_properties()` to map grid dimensions to available hardware. The 2D grid strategy (blocks over M, groups over N) enables efficient parallelization across multiple vector cores while respecting the 64KB per-feature fusion limit. This enables efficient FLA inference on Ascend NPUs by offloading a key non-attention compute pattern.

## Related
- `technique-operator-fusion`
- `hw-vector-unit`
- `kernel-layernorm`
- `technique-flash-attention`