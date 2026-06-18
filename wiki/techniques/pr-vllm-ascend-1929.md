---
id: technique-pr-vllm-ascend-1929
title: "PR Insight: vllm-project/vllm-ascend #1929"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen2.5-vl
  - vit
  - sequence-parallel
  - mrrope
  - fused-ops
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1929"
---

# PR Insight: vllm-project/vllm-ascend #1929

**Title:** qwen2.5-vl Vit module enable sp and mrope fusion op

## Overview
This PR enables sequence parallelism and MRoPE (Multi-Resolution RoPE) NPU fusion operations for the Qwen2.5-VL ViT (Vision Transformer) module, improving performance for vision-language models.

## Technical Significance
Vision model optimization for Ascend. Enabling sequence parallelism and MRoPE fusion for the ViT module reduces communication overhead and operator fusion improves efficiency for the multi-resolution attention pattern in vision-language models.

## Related
- `kernel-attention-ascendc`
- `technique-sequence-parallel`
- `technique-mrrope`
- `technique-operator-fusion`
- `technique-vision-transformer`