---
id: technique-pr-sgl-kernel-npu-405
title: "PR Insight: sgl-project/sgl-kernel-npu #405"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qkv-fusion
  - gemma-rmsnorm
  - rope
  - qwen3-next
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/405"
---

# PR Insight: sgl-project/sgl-kernel-npu #405

**Title:** for qwen3-next:add kernel fused split qkvgate gemma rmsnorm rope

## Overview
This PR adds a fused kernel for Qwen3-Next and Coder Next that combines split (Q, K, V, gate), reshape, Gemma RMS normalization, and RoPE operations. The implementation achieves significant performance improvements, reducing profiling time from 100μs to 40μs per operation.

## Technical Significance
Fusing multiple preprocessing operations (QKV splitting, gating, Gemma-style normalization, and rotary position encoding) into a single kernel dramatically reduces kernel launch overhead and memory access patterns. This optimization is particularly valuable for Qwen3-Next models that require these specific transformations before attention computation.

## Related
- `kernel-qkv-fusion`, `kernel-rmsnorm`, `kernel-rope`, `kernel-gemma-norm`, `technique-operator-fusion`