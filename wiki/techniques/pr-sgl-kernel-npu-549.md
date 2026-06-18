---
id: technique-pr-sgl-kernel-npu-549
title: "PR Insight: sgl-project/sgl-kernel-npu #549"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - deepep
  - quantization
  - fp8
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/549"
---

# PR Insight: sgl-project/sgl-kernel-npu #549

**Title:** feat: add MXFP8 support for low_latency_dispatch

## Overview
This PR adds MXFP8 quantization support to the low-latency dispatch mode in DeepEP. The implementation includes A5-specific kernel optimizations, updated tiling configurations, and comprehensive testing for MXFP8 dispatch operations. The changes enable low-latency MoE inference to leverage mixed-precision quantization for improved memory efficiency and performance.

## Technical Significance
Extending MXFP8 support to low-latency dispatch enables more efficient MoE inference deployment in latency-sensitive scenarios. The combination of low-latency operation and mixed-precision quantization provides both fast response times and reduced memory footprint, which is essential for real-time inference applications. The A5-specific optimizations ensure maximum performance on targeted hardware platforms.

## Related
- `technique-quantization`
- `technique-moe-dispatch`
- `format-mxfp8`
- `pattern-low-latency`