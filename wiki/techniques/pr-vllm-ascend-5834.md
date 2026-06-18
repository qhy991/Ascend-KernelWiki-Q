---
id: technique-pr-vllm-ascend-5834
title: "PR Insight: vllm-project/vllm-ascend #5834"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - refactor
  - attention
  - kv-cache
  - mla
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5834"
---

# PR Insight: vllm-project/vllm-ascend #5834

**Title:** [Refactor] Move AttentionSpec initialization to Attention module

## Overview
This PR refactors the `get_kv_cache_spec` method to delegate AttentionSpec creation to each attention module's own `get_kv_cache_spec()` method. This aligns with vLLM source code structure and simplifies the model runner by removing manual AttentionType checks and centralized spec creation.

## Technical Significance
The refactoring improves code organization and maintainability by following the single responsibility principle. Each attention module (Attention, MambaBase, MLAAttention) now manages its own KV cache spec creation. The fix also preserves Ascend-specific handling, such as the `use_sparse` hack for MLAAttention in DeepSeek DSA mode. This change is part of RFC #5463 item 12 and reduces code duplication in model_runner_v1.py and cpu_offload_connector.py.

## Related
- `technique-mla`, `technique-kv-cache`, `technique-code-refactor`