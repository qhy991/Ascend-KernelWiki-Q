---
id: technique-pr-sgl-kernel-npu-393
title: "PR Insight: sgl-project/sgl-kernel-npu #393"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - scale-shift
  - elementwise
  - multimodal
  - performance-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/393"
---

# PR Insight: sgl-project/sgl-kernel-npu #393

**Title:** add fused scale shift kernel

## Overview
This PR adds a fused_scale_shift kernel for elementwise scale and shift operations, optimizing performance for multimodal generation tasks like Wan2.2. The implementation achieves significant latency improvements, reducing inference time from 115s to 108s in production benchmarks.

## Technical Significance
The fused scale-shift operator eliminates separate scale and shift kernel launches, reducing kernel overhead for multimodal data processing. This optimization is particularly valuable for video generation and other multimodal applications where repeated scale-shift operations are applied during data transformation.

## Related
- `kernel-scale-shift`, `kernel-elementwise`, `technique-operator-fusion`, `technique-multimodal-optimization`