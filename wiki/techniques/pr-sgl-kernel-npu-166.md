---
id: technique-pr-sgl-kernel-npu-166
title: "PR Insight: sgl-project/sgl-kernel-npu #166"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moe
  - low-latency
  - dispatch
  - combine
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/166"
---

# PR Insight: sgl-project/sgl-kernel-npu #166

**Title:** Added custom low_latency operators for dispatch/combine in the A2 dec...

## Overview
Implements custom low-latency dispatch and combine operators specifically optimized for A2 architecture in the DeepEP framework. The operators support hierarchical implementation when HCCL_INTRA_PCIE_ENABLE=1, with additional parameters like topk_weights and expand_scales for improved performance.

## Technical Significance
This is a major optimization for A2 architecture MoE inference, providing specialized low-latency operators that significantly reduce dispatch and combine latency. The hierarchical implementation optimizes for single-server deployments, while the custom parameters enable more efficient weight handling and scale operations. The implementation includes comprehensive CMake build system and tiling utilities for efficient kernel compilation.

## Related
- `wiki-kernel-moe`
- `wiki-technique-hccl-optimization`
- `wiki-hardware-a2`
- `wiki-technique-low-latency`