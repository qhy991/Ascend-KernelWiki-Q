---
id: technique-pr-vllm-ascend-3106
title: "PR Insight: vllm-project/vllm-ascend #3106"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - initialization
  - refactoring
  - code-cleanup
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3106"
---

# PR Insight: vllm-project/vllm-ascend #3106

**Title:** [ModelRunner][Refactor] Refactor kv cache tensor initialization logic

## Overview
This PR refactors KV cache tensor initialization logic by unifying the handling for DeepSeek and normal models. It splits initialize_kv_cache_tensors into _allocate_kv_cache_tensors and _reshape_kv_cache_tensors, following the GPU model runner pattern in vLLM.

## Technical Significance
Refactoring improves code maintainability and consistency with upstream vLLM. Separating allocation and reshaping logic makes the code more modular and easier to understand. The unification ensures consistent KV cache handling across different model architectures.

## Related
- `technique-kv-cache-paging`, `pattern-code-refactoring`, `kernel-deepseek-ascendc`