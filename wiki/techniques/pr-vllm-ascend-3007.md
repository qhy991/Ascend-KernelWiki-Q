---
id: technique-pr-vllm-ascend-3007
title: "PR Insight: vllm-project/vllm-ascend #3007"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hybrid-kv-cache
  - pd-separation
  - qwen3-next
  - memory-alignment
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3007"
---

# PR Insight: vllm-project/vllm-ascend #3007

**Title:** [HybridKV] Fix prefill disaggregation kvcache addr alignment & use hybrid kv cache only when running qwen3_next

## Overview
This PR fixes three prefill disaggregation issues: KV cache address alignment (requires 2M alignment for llmdatadist), KV cache shape errors (should be [num_blocks, ...] not [2, num_blocks, ...]), and accuracy issues by using hybrid KV cache only for qwen3_next models.

## Technical Significance
The fixes address critical correctness issues in disaggregated prefill scenarios. Memory alignment and correct tensor shapes are essential for llmdatadist compatibility. The hybrid KV cache restriction to qwen3_next prevents accuracy issues in other models, showing that hybrid KV optimizations are model-specific.

## Related
- `technique-hybrid-kv-cache`, `technique-pd-separation`, `kernel-qwen3-next-ascendc`