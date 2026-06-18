---
id: technique-pr-sgl-kernel-npu-36
title: "PR Insight: sgl-project/sgl-kernel-npu #36"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - combine
  - moe
  - prefill
  - ascendc
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/36"
---

# PR Insight: sgl-project/sgl-kernel-npu #36

**Title:** add combine normal kernel for prefill moe stage

## Overview
This PR adds AscendC kernel implementation for normal MoE combine operations during the prefill stage. Includes comprehensive tiling logic (546 lines), kernel implementation (387 lines), and ACLNN API integration for cam_moe_combine_normal operator.

## Technical Significance
Provides optimized MoE result aggregation for prefill stage inference on Ascend NPUs. The combine kernel merges expert outputs efficiently with tiling optimizations for memory bandwidth. Complements the dispatch kernel (PR #34) to complete the MoE inference pipeline.

## Related
- technique-moe-combine
- technique-prefill-optimization
- technique-combine-kernel
- technique-ascendc