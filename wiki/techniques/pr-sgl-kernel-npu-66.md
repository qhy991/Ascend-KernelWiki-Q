---
id: technique-pr-sgl-kernel-npu-66
title: "PR Insight: sgl-project/sgl-kernel-npu #66"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - dispatch
  - quantization
  - performance
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/66"
---

# PR Insight: sgl-project/sgl-kernel-npu #66

**Title:** normal_dispatch enable quant

## Overview
This PR enables quantization support for normal dispatch operations in Deep EP. Updates deep_ep.cpp, deep_ep.hpp, and buffer.py to support quantized data types. Benchmarks show 52% latency improvement (4210us vs 6416us) and 52% bandwidth improvement (111 vs 73 GB/s) for dispatch operations.

## Technical Significance
Achieves significant performance improvements for MoE dispatch operations through quantization. Quantization reduces memory bandwidth requirements and improves compute efficiency, particularly beneficial for memory-bound dispatch operations. This optimization is critical for scaling MoE inference on Ascend hardware.

## Related
- technique-quantization
- technique-dispatch-optimization
- technique-memory-bandwidth