---
id: technique-pr-vllm-ascend-4750
title: "PR Insight: vllm-project/vllm-ascend #4750"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mm-encoder
  - custom-op
  - qwen-vl
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4750"
---

# PR Insight: vllm-project/vllm-ascend #4750

**Title:** [CustomOp] Register AscendMMEncoderAttention CustomOp and remove related patch

## Overview
This PR registers `AscendMMEncoderAttention` as a CustomOp and removes related patches for Qwen2.5-VL and Qwen3-VL models. It cleans up the patch system by moving the multimodal encoder attention implementation to a proper CustomOp registration in vllm_ascend/ops/mm_encoder_attention.py.

## Technical Significance
Migrates from patch-based customization to proper CustomOp registration, which is the upstream vLLM standard. This improves code maintainability and follows vLLM's extensibility model. The change affects multimodal vision-language models (Qwen2.5-VL, Qwen3-VL) that use encoder attention for vision token processing.

## Related
- `kernel-mm-encoder-attention`
- `technique-custom-op`
- `kernel-attention`
- `technique-vl-models`