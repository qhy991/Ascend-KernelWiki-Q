---
id: technique-pr-vllm-ascend-5723
title: "PR Insight: vllm-project/vllm-ascend #5723"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - quantization
  - mxfp8
  - qwen
  - dense
  - linear
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5723"
---

# PR Insight: vllm-project/vllm-ascend #5723

**Title:** support mxfp8 quantization (qwen dense)

## Overview
This PR adds MXFP8 quantization support for Qwen dense models, implementing a new quantization configuration and utility functions in the quantization module. The implementation extends the existing quantization infrastructure to handle MXFP8 format, adding `w8a8mxfp8.py` with configuration parsing and weight handling for MXFP8-quantized linear layers. The changes update `quant_config.py` and `utils.py` to support the new format.

## Technical Significance
This PR enables MXFP8 quantization for Qwen dense models, expanding the quantization format support in VLLM Ascend beyond traditional W8A8 and W4A16 schemes. MXFP8 is a specialized floating-point 8-bit format that can provide better accuracy than integer quantization for some models. The implementation integrates with the existing quantization infrastructure, allowing users to leverage MXFP8's benefits while maintaining compatibility with VLLM's Ascend backend for dense model inference.

## Related
- `technique-quantization`, `technique-mxfp8`, `technique-w8a8`