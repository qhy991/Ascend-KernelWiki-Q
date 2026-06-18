---
id: technique-pr-vllm-ascend-6610
title: "PR Insight: vllm-project/vllm-ascend #6610"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - mla
  - deepseek-v3.2
  - memory-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6610"
---

# PR Insight: vllm-project/vllm-ascend #6610

**Title:** [refactor]Optimized the kvcache usage of Deepseek v3.2

## Overview
This PR optimizes KV cache allocation for DeepSeek v3.2 models using sparse attention by replacing FullAttentionSpec with MLAAttentionSpec and introducing principled calculation of KV cache tensor split factors based on model configuration instead of hardcoded values.

## Technical Significance
Significantly improves KV cache memory utilization for DeepSeek v3.2 from 15,872 to 25,984 tokens on a single A3 server, reducing waste by ~38.8%. The fix correctly sizes cache tensors based on actual K cache usage patterns in MLA attention, improving inference throughput and memory efficiency.

## Related
- `technique-kv-cache-paging`