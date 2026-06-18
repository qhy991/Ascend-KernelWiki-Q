---
id: technique-pr-vllm-ascend-4199
title: "PR Insight: vllm-project/vllm-ascend #4199"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-moe
  - cudagraph
  - performance
  - configuration
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4199"
---

# PR Insight: vllm-project/vllm-ascend #4199

**Title:** [main][misc]change default capture size for Qwen3-MoE when using full dp

## Overview
This PR changes the default `cudagraph_capture_size` for Qwen3-MoE when running in full DP (dp_size > 1 && tp_size == 1), which is typically used in Large-Scale EP. The old default `[1, 2, 4, 8, 16, 24, ...]` is changed to `[1, 2, 5, 10, 15, 16, 24, ...]` because the `_npu_paged_attention` operator performance degrades significantly with the old settings.

## Technical Significance
Graph capture size configuration significantly impacts performance on Ascend NPUs. The optimized capture sizes for Qwen3-MoE in full DP scenarios provide better performance by aligning with the operator's optimal batch size ranges. This provides out-of-the-box performance for users without requiring manual tuning.

## Related
- `technique-cudagraph`, `technique-moe`, `technique-qwen3-moe`, `pattern-performance-tuning`, `technique-full-dp`