---
id: technique-pr-sgl-kernel-npu-404
title: "PR Insight: sgl-project/sgl-kernel-npu #404"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - split-qkv
  - rmsnorm
  - rope
  - graph-capture
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/404"
---

# PR Insight: sgl-project/sgl-kernel-npu #404

**Title:** add split_qkv_rmsnorm_rope_pos_cache_half_npu test case and fix graph capture bug

## Overview
This PR fixes a graph capture bug in split_qkv_rmsnorm_rope_pos_cache_half_npu where host-side position validation triggered device sync, breaking torch.npu.graph capture. The fix moves bounds checking into the kernel, clamping positions to [0, max_seq-1] before indexing cos/sin cache. Comprehensive tests include golden reference, eager comparison, and NPUGraph capture/replay validation.

## Technical Significance
Making the operator graph-safe enables its use in torch.npu.graph for static graph optimization, which is critical for production inference performance. The on-device bounds checking approach maintains safety while avoiding device sync that prevents graph capture, enabling broader deployment scenarios.

## Related
- `kernel-split-qkv`, `kernel-rmsnorm`, `kernel-rope`, `technique-graph-optimization`, `technique-bugfix`