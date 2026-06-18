---
id: technique-pr-sgl-kernel-npu-499
title: "PR Insight: sgl-project/sgl-kernel-npu #499"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - a2
  - cann9.0
  - adapter
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/499"
---

# PR Insight: sgl-project/sgl-kernel-npu #499

**Title:** 【DeepEP】a2 cann9.0 adapter

## Overview
This PR adapts DeepEP for A2 hardware with CANN 9.0 compatibility. The modifications update kernel compilation and build configurations to ensure proper operation with the newer CANN version while maintaining A2-specific optimizations and performance characteristics.

## Technical Significance
Adapting DeepEP for CANN 9.0 ensures compatibility with the latest CANN toolkit while preserving optimizations for A2 hardware. This adaptation allows users to benefit from CANN 9.0 improvements while maintaining DeepEP's efficient MoE routing and execution capabilities on A2 platforms.

## Related
- `kernel-deepep-a2`, `technique-cann-compatibility`, `technique-version-adaptation`