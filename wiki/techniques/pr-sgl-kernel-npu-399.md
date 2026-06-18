---
id: technique-pr-sgl-kernel-npu-399
title: "PR Insight: sgl-project/sgl-kernel-npu #399"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gated-delta-rule
  - recurrent
  - qwen3-next
  - attention
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/399"
---

# PR Insight: sgl-project/sgl-kernel-npu #399

**Title:** add recurrent_gated_delta_rule kernel

## Overview
This PR adds a recurrent_gated_delta_rule kernel for Qwen3-Next models, implementing the recurrent gated delta rule attention mechanism in AscendC. The kernel includes comprehensive host-side inference, tiling, and kernel implementations with tensor utility functions for efficient recurrent attention computation.

## Technical Significance
Implementing recurrent gated delta rule in AscendC provides optimized performance for models using this attention mechanism, particularly beneficial for Qwen3-Next architecture. The kernel enables efficient stateful attention computation with proper tensor manipulation and memory management.

## Related
- `kernel-recurrent-gated-delta-rule`, `kernel-gated-delta-rule`, `kernel-fla-recurrent`