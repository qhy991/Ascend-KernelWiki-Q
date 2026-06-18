---
id: technique-pr-vllm-ascend-6828
title: "PR Insight: vllm-project/vllm-ascend #6828"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8
  - qwen-omni
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6828"
---

# PR Insight: vllm-project/vllm-ascend #6828

**Title:** [Model]Add Qwen3-Omni quantization Ascend NPU adaptation and optimization

## Overview
This PR adds operator-level quantization adaptation and Auto-Quantization Tuning (AUT) component optimization for Qwen3-Omni multimodal models on Ascend NPU. The implementation uses patch-based modifications to integrate quantization support, affecting the w8a8_dynamic quantization method and ModelSlim configuration systems.

## Technical Significance
Enables efficient quantized inference for Qwen3-Omni multimodal models on Ascend hardware by adding ModelSlim-compatible quantization configurations. The patch-based approach allows for operator-specific optimizations while maintaining compatibility with the quantization framework.

## Related
- `technique-quantization-w8a8`, `technique-operator-fusion`, `kernel-matmul-ascendc`