---
id: technique-pr-vllm-ascend-204
title: "PR Insight: vllm-project/vllm-ascend #204"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - performance
  - data-reuse
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/204"
---

# PR Insight: vllm-project/vllm-ascend #204

**Title:** [Performance] Change the shape of kv_cache to avoid view of k_cache and v_cache.

## Overview
This PR restructures KV cache shapes to avoid tensor views, and caches K/V metadata to eliminate redundant slice operations. Changes span attention.py, quantization config, and worker initialization.

## Technical Significance
Tensor views can cause memory layout issues and prevent kernel optimizations. Reshaping KV caches to be contiguous and caching metadata reduces per-step overhead, improving attention performance. This is particularly important for quantized KV caches.

## Related
- kernel-attention
- technique-kv-cache-paging
- technique-data-reuse