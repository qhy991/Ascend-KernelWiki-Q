---
id: technique-pr-sgl-kernel-npu-34
title: "PR Insight: sgl-project/sgl-kernel-npu #34"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - dispatch
  - moe
  - prefill
  - ascendc
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/34"
---

# PR Insight: sgl-project/sgl-kernel-npu #34

**Title:** add dispatch normal kernel for prefill moe stage

## Overview
This PR adds a comprehensive AscendC kernel implementation for normal MoE dispatch operations during the prefill stage. Includes extensive CMake build infrastructure, tiling logic (635 lines), and ACLNN API integration for cam_moe_dispatch_normal operator.

## Technical Significance
Provides optimized MoE expert routing for prefill stage inference on Ascend NPUs. The kernel implements efficient token-to-expert dispatch with tiling optimizations for memory bandwidth. The build infrastructure enables automated compilation of AscendC kernels for Deep EP MoE workloads.

## Related
- technique-moe-routing
- technique-prefill-optimization
- technique-dispatch-kernel
- technique-ascendc