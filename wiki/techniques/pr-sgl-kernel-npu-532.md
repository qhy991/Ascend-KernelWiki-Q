---
id: technique-pr-sgl-kernel-npu-532
title: "PR Insight: sgl-project/sgl-kernel-npu #532"
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
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/532"
---

# PR Insight: sgl-project/sgl-kernel-npu #532

**Title:** add a5 mxfp8 for dispatch normal

## Overview
This PR adds MXFP8 (Mixed-Precision FP8) quantization support for the normal dispatch mode on A5 hardware. The implementation includes new quantization functions, updated tiling configurations, and strategy modifications to enable MXFP8 data format support. The changes span kernel implementations, host code, and Python strategy layers for comprehensive MXFP8 integration.

## Technical Significance
MXFP8 support for normal dispatch enables more efficient memory usage and computation for MoE inference on A5 hardware. Mixed-precision quantization reduces memory bandwidth requirements while maintaining model accuracy, which is crucial for deploying large-scale MoE models. The integration across all layers (kernel, host, strategy) ensures proper handling of quantized data throughout the inference pipeline.

## Related
- `technique-quantization`
- `technique-moe-dispatch`
- `format-mxfp8`
- `pattern-mixed-precision`