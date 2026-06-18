---
id: technique-pr-sgl-kernel-npu-467
title: "PR Insight: sgl-project/sgl-kernel-npu #467"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - a5
  - adaptation
  - build-system
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/467"
---

# PR Insight: sgl-project/sgl-kernel-npu #467

**Title:** Adaptation of the Deepep A5 normal and low-latency operators.

## Overview
This PR adapts DeepEP normal and low-latency operators for Ascend A5 hardware, including comprehensive kernel implementations, build system modifications, and documentation updates. The adaptation adds A5-specific optimizations for dispatch, combine, and notify operations with proper tiling and memory management.

## Technical Significance
Adapting DeepEP for A5 hardware expands support to newer Ascend chip generations, enabling the performance benefits of DeepEP MoE operators on the latest hardware. The implementation includes hardware-specific optimizations that leverage A5's capabilities while maintaining compatibility with existing DeepEP interfaces.

## Related
- `kernel-deepep-normal`, `kernel-deepep-low-latency`, `kernel-deepep-a5`, `technique-hardware-adaptation`