---
id: technique-pr-sgl-kernel-npu-107
title: "PR Insight: sgl-project/sgl-kernel-npu #107"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - layout
  - nz-format
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/107"
---

# PR Insight: sgl-project/sgl-kernel-npu #107

**Title:** unfold layout expert limit and fix bug

## Overview
This PR removes layout expert limit constraints and fixes bugs in the dispatch layout tiling and kernel code. The changes affect how token layouts are organized across experts in MoE dispatch operations.

## Technical Significance
Unfolding expert limits enables more flexible expert routing and better load balancing in MoE systems. Layout optimizations are crucial for NZ format data access patterns on Ascend, as proper tiling ensures efficient memory access and Cube unit utilization.

## Related
- `technique-moe`, `technique-nz-tiling`, `hw-nz-format`