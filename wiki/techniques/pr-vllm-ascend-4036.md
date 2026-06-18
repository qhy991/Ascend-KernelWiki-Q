---
id: technique-pr-vllm-ascend-4036
title: "PR Insight: vllm-project/vllm-ascend #4036"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8
  - compressed-tensors
  - llm-compressor
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4036"
---

# PR Insight: vllm-project/vllm-ascend #4036

**Title:** [Quantization] Support compressed tensors w8a8 static and w8a8 dynamic weight

## Overview
This PR adds support for LLM Compressor quantization format with W8A8 static and W8A8 dynamic weights. The changes include: (1) AscendCompressedTensorsConfig to replace CompressedTensorsConfig, (2) W8A8 static weight support (weight: per-channel int8 symmetric, activation: per-tensor int8 symmetric), (3) W8A8Dynamic weight support (weight: per-channel int8 symmetric, activation: per-token int8 symmetric dynamic), (4) Modification of override_quantization_method in AscendQuantConfig.

## Technical Significance
Support for LLM Compressor format enables vLLM Ascend to work with weights quantized using the popular LLM Compressor tool. W8A8 quantization provides significant memory savings with minimal accuracy loss. Supporting both static and dynamic quantization modes gives flexibility for different deployment scenarios. The per-token dynamic mode is particularly valuable for maintaining accuracy while reducing memory footprint.

## Related
- `technique-quantization`, `technique-w8a8`, `pattern-weight-compression`, `technique-dynamic-quantization`