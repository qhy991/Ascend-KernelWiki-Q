---
id: technique-pr-vllm-ascend-5837
title: "PR Insight: vllm-project/vllm-ascend #5837"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - bugfix
  - cp
  - chunked-prefill
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5837"
---

# PR Insight: vllm-project/vllm-ascend #5837

**Title:** [bugfix](cp) replace None with zeros/inf tensor to avoid TypeError

## Overview
This PR fixes a TypeError in context parallel scenarios where some devices have no KV cache data. The `_compute_prefill_context` function was returning None for empty KV caches, which caused downstream errors. The fix replaces None returns with properly shaped zero or negative infinity tensors.

## Technical Significance
In CP (Context Parallel) setups with chunked prefill, some devices may not receive any KV cache segments for certain requests. Returning None caused TypeErrors when tensor operations were attempted. The fix ensures all devices return tensors with appropriate values (zeros for normal data, -inf for attention masks), maintaining consistent tensor shapes across all ranks. This enables robust chunked prefill with empty KV cache scenarios in multi-card deployments.

## Related
- `technique-context-parallel`, `technique-chunked-prefill`, `technique-kv-cache`