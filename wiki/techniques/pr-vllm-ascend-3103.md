---
id: technique-pr-vllm-ascend-3103
title: "PR Insight: vllm-project/vllm-ascend #3103"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-vl
  - vision-language
  - model-support
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3103"
---

# PR Insight: vllm-project/vllm-ascend #3103

**Title:** [Model]Add support for qwen3_vl and qwen3_vl_moe

## Overview
This PR adds support and optimization for Qwen3-VL and Qwen3-VL-MoE models on the Ascend platform. The adaptation enables vision-language model inference on Ascend NPUs with platform-specific optimizations.

## Technical Significance
Vision-language models require handling both image and text modalities, adding complexity to attention mechanisms and memory management. Platform-specific optimizations for Qwen3-VL models enable efficient deployment of multi-modal AI workloads on Ascend hardware.

## Related
- `kernel-qwen3-vl-ascendc`, `kernel-vision-attention-ascendc`, `pattern-vl-model-optimization`