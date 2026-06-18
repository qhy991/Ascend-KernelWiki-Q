---
id: technique-pr-vllm-ascend-3366
title: "PR Insight: vllm-project/vllm-ascend #3366"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - kv-cache
  - mooncake
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3366"
---

# PR Insight: vllm-project/vllm-ascend #3366

**Title:** [Bugfix][P/D] TP size larger than KV cache head causes accuracy issues

## Overview
Resolve the issue where, in the case of unequal TP (Tensor Parallelism), the TP size  is larger than the number of model attention kvcache heads, causing the KV cache to generate duplicates, which leads to transmission errors in the original code.

## Technical Significance
Fixes accuracy issues caused by TP size being larger than KV cache head count in parallel/distributed deployment scenarios.

## Related
- `technique-kv-cache-paging`
- `technique-hccl-optimization`
- `technique-distributed-inference`
