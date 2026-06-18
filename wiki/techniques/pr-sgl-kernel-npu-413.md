---
id: technique-pr-sgl-kernel-npu-413
title: "PR Insight: sgl-project/sgl-kernel-npu #413"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - split-qkv
  - rmsnorm
  - rope
  - tensor-parallelism
  - minimax
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/413"
---

# PR Insight: sgl-project/sgl-kernel-npu #413

**Title:** add split_qkv_tp_rmsnorm_rope ops

## Overview
This PR adds split_qkv_tp_rmsnorm_rope operations for tensor parallelism (TP) scenarios in MiniMax models. The implementation supports RMS normalization with tensor-parallel QKV splitting and rotary position encoding, enabling efficient distributed execution of attention layers across multiple devices.

## Technical Significance
Adding tensor-parallel QKV splitting with normalization enables efficient distributed training and inference for models using tensor parallelism. The operator supports the specific requirements of MiniMax models while providing a general solution for TP-based attention computation with proper normalization and position encoding.

## Related
- `kernel-split-qkv`, `kernel-rmsnorm`, `kernel-rope`, `technique-tensor-parallelism`