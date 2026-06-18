---
id: technique-pr-vllm-ascend-2913
title: "PR Insight: vllm-project/vllm-ascend #2913"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - mooncake
  - distributed
  - store
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2913"
---

# PR Insight: vllm-project/vllm-ascend #2913

**Title:** [Feat] A Connector that supports Mooncake store

## Overview
This PR adds a Mooncake store connector to enable KV cache reuse in scenarios with system prompts or multi-turn dialogues. It includes configuration data, KV transfer logic, MoonCake engine, store implementation, and v1 connector.

## Technical Significance
The Mooncake store connector provides persistent KV cache storage, allowing reuse across requests with overlapping contexts. This reduces redundant computation for system prompts and enables more efficient multi-turn dialogue scenarios. The implementation includes comprehensive configuration management and data transfer protocols for distributed inference.

## Related
- `technique-kv-cache-paging`, `pattern-mooncake-connector`, `technique-distributed-inference`