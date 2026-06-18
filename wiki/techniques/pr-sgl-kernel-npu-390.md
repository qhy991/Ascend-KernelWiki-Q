---
id: technique-pr-sgl-kernel-npu-390
title: "PR Insight: sgl-project/sgl-kernel-npu #390"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - split-qkv
  - rmsnorm
  - rope
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/390"
---

# PR Insight: sgl-project/sgl-kernel-npu #390

**Title:** [feat] add Split qkv rms norm half rope op

## Overview
This PR adds a Triton implementation of the split_qkv_rmsnorm_rope_pos_cache_half_npu operator for accelerated QKV splitting, RMS normalization, and rotary position encoding with half-precision cos/sin cache. The operator is designed for LLaDA2 model acceleration and integrates with sglang-ascend's rotary embedding module.

## Technical Significance
Fusing QKV splitting, RMS normalization, and RoPE operations into a single kernel reduces memory access overhead and improves performance for transformer attention layers. The half-precision cos/sin cache optimization further reduces memory bandwidth requirements while maintaining numerical accuracy for position encoding.

## Related
- `kernel-split-qkv`, `kernel-rmsnorm`, `kernel-rope`, `technique-operator-fusion`