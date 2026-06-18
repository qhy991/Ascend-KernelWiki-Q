---
id: technique-pr-vllm-ascend-2019
title: "PR Insight: vllm-project/vllm-ascend #2019"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - torchair
  - dynamo
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2019"
---

# PR Insight: vllm-project/vllm-ascend #2019

**Title:** [0.9.1][feat] add kv cache memory cache and skip dynamo guard for deepseek and deepseek_mtp models to increase user-friedliness

## Overview
This PR optimizes DeepSeek and MTP (Multimodal Thinking Process) models by adding KV cache memory caching and skipping Dynamo guards. The implementation resets the Dynamo graph and invokes the `cache_compile` API twice, reducing TPOT by approximately 3ms. Users can enable this feature through `torhcair_graph_config` with `use_cached_graph:true`.

## Technical Significance
This optimization provides significant performance improvements (3ms TPOT reduction) while maintaining user-friendliness through simple configuration. The KV cache memory caching and Dynamo guard skipping improve efficiency for both single-node online serving and multi-node disaggregated prefill scenarios, making it valuable for production DeepSeek deployments.

## Related
- `technique-kv-cache`
- `technique-torchair`
- `technique-deepseek`
- `technique-mtp`