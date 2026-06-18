---
id: technique-pr-vllm-ascend-2947
title: "PR Insight: vllm-project/vllm-ascend #2947"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - gqa
  - mla
  - kv-cache
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2947"
---

# PR Insight: vllm-project/vllm-ascend #2947

**Title:** [Feature] mooncake connector support GQA transport

## Overview
This PR extends the Mooncake connector to support heterogeneous Tensor Parallel (TP) scenarios where Prefill and Decode nodes have different TP sizes. It handles KV cache merging using npu_paged_cache_load and npu_reshape_and_cache operations with minimal transpose overhead.

## Technical Significance
Supporting heterogeneous TP enables more flexible resource allocation in distributed inference. The implementation minimizes transpose overhead by using specialized Ascend operators to extract and rewrite cache blocks, making GQA transport efficient even with layout differences between prefill and decode phases.

## Related
- `technique-kv-cache-paging`, `pattern-mooncake-connector`, `kernel-gqa-ascendc`