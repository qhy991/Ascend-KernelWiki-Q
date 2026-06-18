---
id: technique-pr-sgl-kernel-npu-394
title: "PR Insight: sgl-project/sgl-kernel-npu #394"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qkv-fusion
  - reshape
  - concatenate
  - qwen3-next
  - performance-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/394"
---

# PR Insight: sgl-project/sgl-kernel-npu #394

**Title:** add kernel fused qkvzba split reshape cat

## Overview
This PR adds a fused kernel for QKV, Z, BA split, reshape, and concatenate operations specifically optimized for Qwen3-Next. The implementation achieves significant performance improvements, reducing operation time from 100μs to 40μs per operation during decode and 200μs improvements during prefill phases.

## Technical Significance
Fusing multiple tensor manipulation operations (QKV/ZBA split, reshape, concatenation) into a single kernel reduces memory transfers and kernel launch overhead. This optimization provides substantial latency benefits for models like Qwen3-Next that require complex QKV tensor transformations during attention computation.

## Related
- `kernel-qkv-fusion`, `kernel-reshape`, `kernel-concatenate`, `technique-operator-fusion`