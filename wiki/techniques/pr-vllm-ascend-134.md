---
id: technique-pr-vllm-ascend-134
title: "PR Insight: vllm-project/vllm-ascend #134"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - kv-cache
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/vllm-ascend/pull/134"
---

# PR Insight: vllm-project/vllm-ascend #134

**Title:** [BugFix] add int8 cache dtype && modify initialization of attention

## Overview
This PR adds int8 cache dtype support to vllm-ascend by extending STR_DTYPE_TO_TORCH_DTYPE mapping and adding a patch module for cache dtype handling. Ascend attention requires int8 KV cache dtype for quantization support.

## Technical Significance
Enables int8 quantization for KV caches on Ascend, critical for memory reduction in long-context scenarios. The patch approach allows extending vLLM's dtype mapping without modifying upstream code, maintaining compatibility while adding Ascend-specific requirements.

## Related
- technique-quantization
- technique-kv-cache-paging