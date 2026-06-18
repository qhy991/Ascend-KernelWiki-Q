---
id: technique-pr-vllm-ascend-6887
title: "PR Insight: vllm-project/vllm-ascend #6887"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - hybrid-attention
  - qwen
  - mamba
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6887"
---

# PR Insight: vllm-project/vllm-ascend #6887

**Title:** [KVCache]Qwen3.5 supports contiguous tensor hybrid-attn kv-cache

## Overview
Supports contiguous tensor hybrid-attention KV cache for Qwen3.5 and Qwen3Next models that use full attention + Mamba hybrid architectures. Due to Ascend operator restrictions requiring contiguous tensors, the implementation uses a multi-tensor scheme where KV tensors, conv tensors, and SSM tensors are arranged to guarantee contiguity.

## Technical Significance
Enables efficient KV cache management for hybrid attention models on Ascend hardware by working around operator contiguity requirements. The multi-tensor layout scheme ensures all cache tensors remain contiguous while accommodating different tensor types (KV, conv, SSM).

## Related
- `technique-kv-cache`, `technique-hybrid-attention`, `technique-mamba`, `technique-contiguous-layout`