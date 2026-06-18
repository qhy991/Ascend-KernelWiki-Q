---
id: technique-pr-vllm-ascend-9721
title: "PR Insight: vllm-project/vllm-ascend #9721"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - quantization
  - kv-cache
  - nz-format
  - c8
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9721"
---

# PR Insight: vllm-project/vllm-ascend #9721

**Title:** [Feature]Add NZ layout support for C8 quantization(GQA)

## Overview
This PR adds NZ layout support for C8 quantization of KV cache, converting KV cache from ND layout to NZ layout during C8 quantization to improve memory access efficiency and computational performance for attention operations.

## Technical Significance
Improves throughput by ~90% compared to the previous version for Qwen3-32B-w8a8c8 on 910B3×4. NZ layout optimization provides better memory access patterns for attention operations on Ascend NPUs, particularly beneficial for GQA configurations with quantized KV caches.

## Related
- `technique-quantization`, `technique-nz-format`, `kernel-attention`, `kernel-gqa`