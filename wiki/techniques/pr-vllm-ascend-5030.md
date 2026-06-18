---
id: technique-pr-vllm-ascend-5030
title: "PR Insight: vllm-project/vllm-ascend #5030"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-pool
  - kv-cache
  - tp
  - mla
  - gqa
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5030"
---

# PR Insight: vllm-project/vllm-ascend #5030

**Title:** [bugfix] [main] Fix KV cache query inconsistency across different TP ranks in the KV Pool

## Overview
This PR fixes KV cache query inconsistency across TP ranks in the KV Pool for MLA and GQA models where identical KV caches are generated. The previous approach allowed each rank to query storage dynamically, causing inconsistent results and incorrect storage. The new solution pre-allocates storage responsibilities so each rank stores its pre-assigned blocks directly.

## Technical Significance
Ensures correct KV cache storage and retrieval in KV Pool when using tensor parallelism with models that generate identical KV caches across ranks. Eliminates data inconsistencies caused by dynamic querying.

## Related
- `kernel-kv-pool`
- `technique-kv-cache-sharing`
- `kernel-mla`
- `kernel-gqa`
- `technique-tensor-parallelism`