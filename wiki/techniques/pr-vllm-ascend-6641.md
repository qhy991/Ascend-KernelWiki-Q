---
id: technique-pr-vllm-ascend-6641
title: "PR Insight: vllm-project/vllm-ascend #6641"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - moe
  - quantization
  - w8a8
  - dynamic-quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6641"
---

# PR Insight: vllm-project/vllm-ascend #6641

**Title:** [Feat] 310p support MoE W8A8 quantizaition

## Overview
This PR adds W8A8 dynamic quantization support for MoE models on Ascend 310P. It implements AscendW8A8DynamicFusedMoEMethod310, a unified MLP implementation handling both quantized and unquantized paths, and adds comprehensive e2e and unit tests.

## Technical Significance
Enables efficient quantized MoE inference on Ascend 310P hardware with platform-specific optimizations. The dynamic quantization approach provides flexibility while maintaining performance for MoE expert computations on edge devices.

## Related
- `kernel-moe`
- `technique-quantization`