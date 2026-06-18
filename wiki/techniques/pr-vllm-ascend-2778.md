---
id: technique-pr-vllm-ascend-2778
title: "PR Insight: vllm-project/vllm-ascend #2778"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - quantization
  - w8a8
  - qwen-vl
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2778"
---

# PR Insight: vllm-project/vllm-ascend #2778

**Title:** support qwen25 vl w8a8 quantization

## Overview
This PR adds W8A8 quantization support for Qwen2.5 Vision-Language (VL) models. The implementation includes quantization configuration updates and enables efficient inference of multimodal models with reduced memory footprint on Ascend NPU.

## Technical Significance
Vision-language models require specialized handling for both text and vision components. W8A8 quantization support enables efficient deployment of Qwen2.5 VL models on Ascend NPU, reducing memory requirements while maintaining accuracy for multimodal inference workloads.

## Related
- `technique-quantization`
- `kernel-qwen2-5-vl`
- `kernel-quantization`
- `technique-multimodal`