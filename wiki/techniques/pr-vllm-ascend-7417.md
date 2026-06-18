---
id: technique-pr-vllm-ascend-7417
title: "PR Insight: vllm-project/vllm-ascend #7417"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen-vl
  - w8a8mxfp8
  - quantization
  - tensor-reshaping
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7417"
---

# PR Insight: vllm-project/vllm-ascend #7417

**Title:** Adapt w8a8mxfp8 quantization for Qwen VL models

## Overview
This PR adapts the w8a8_mxfp8 quantization method for Qwen Vision-Language models. Key changes include reshaping multi-dimensional input tensors to 2D before quantized matmul, reshaping output back to original format, handling visual component output reshaping, and casting bias to float32 for npu_quant_matmul kernel requirements.

## Technical Significance
This extension matters for enabling MXFP8 quantization on multimodal models. Qwen VL models have multi-dimensional visual embeddings that the existing quantization path couldn't handle. The tensor reshaping ensures compatibility with the matmul-based quantization kernel while maintaining correct data layout for visual components, enabling memory-efficient quantized inference for VL models.

## Related
- technique-quantization
- technique-w8a8mxfp8
- technique-vl-inference