---
id: technique-pr-vllm-ascend-6171
title: "PR Insight: vllm-project/vllm-ascend #6171"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - page-size
  - hybrid-kv-cache
  - pd-disaggregation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6171"
---

# PR Insight: vllm-project/vllm-ascend #6171

**Title:** [0.13.0][KVCache] Support different page sizes

## Overview
This PR adds support for different page sizes across KV cache groups and enables hybrid KV cache in prefill disaggregation scenarios. The implementation adds KV cache utility patches and config patches to handle variable page sizes.

## Technical Significance
Different layers in large models have varying optimal page sizes for KV cache management. Supporting multiple page sizes allows fine-grained memory allocation that reduces fragmentation and improves utilization. This is particularly important in prefill-decode disaggregation scenarios where prefill and decode phases have different memory access patterns and requirements.

## Related
- `technique-kv-cache-paging`, `technique-multi-block-pool`, `technique-pd-disaggregation`