---
id: technique-pr-vllm-ascend-7762
title: "PR Insight: vllm-project/vllm-ascend #7762"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3vl
  - qkv-rmsnorm
  - mrope
  - feature
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7762"
---

# PR Insight: vllm-project/vllm-ascend #7762

**Title:** [Feature] support qkv_rmsnorm_mrope for qwen3vl

## Overview
This PR adds support for QKV RMS normalization with multi-resolution RoPE (mRoPE) for Qwen3VL models. The changes affect patch initialization and Qwen3VL-specific worker patching.

## Technical Significance
Enables efficient QKV normalization and multi-resolution position encoding for Qwen3VL vision-language models, supporting variable-resolution vision inputs with proper attention computation.

## Related
- `kernel-layernorm`, `pattern-position-encoding`, `pattern-qwen-architecture`, `pattern-vision-language`, `technique-multi-resolution-encoding`