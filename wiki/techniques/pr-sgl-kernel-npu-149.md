---
id: technique-pr-sgl-kernel-npu-149
title: "PR Insight: sgl-project/sgl-kernel-npu #149"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - layout
  - dispatch
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/149"
---

# PR Insight: sgl-project/sgl-kernel-npu #149

**Title:** add a2 dispatch layout and update its test

## Overview
This PR adds A2-specific dispatch layout implementation with optimized tiling and kernel code. It updates the API, Python bindings, and test infrastructure to support the new layout.

## Technical Significance
A2-specific layouts account for hardware differences between Ascend 910 and 910B variants, ensuring optimal memory access patterns and compute utilization. Custom dispatch layouts are critical for MoE performance as they determine token-to-expert mapping efficiency.

## Related
- `technique-moe`, `technique-layout`, `technique-dispatch`