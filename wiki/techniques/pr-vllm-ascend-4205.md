---
id: technique-pr-vllm-ascend-4205
title: "PR Insight: vllm-project/vllm-ascend #4205"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/4205"
---

# PR Insight: vllm-project/vllm-ascend #4205

**Title:** [v0.11.0-dev][misc]change default capture size for Qwen3-MoE when using full dp

## Overview
This PR is the v0.11.0-dev version of PR #4199, changing the default `cudagraph_capture_size` for Qwen3-MoE in full DP scenarios from `[1, 2, 4, 8, 16, 24, ...]` to `[1, 2, 5, 10, 15, 16, 24, ...]`. The change addresses performance degradation of `_npu_paged_attention` operator with old capture size settings.

## Technical Significance
Consistent performance tuning across branches ensures all vLLM versions benefit from optimized configurations. The capture size optimization is critical for Large-Scale EP deployments using Qwen3-MoE, providing better throughput without user intervention.

## Related
- `technique-cudagraph`, `technique-moe`, `technique-qwen3-moe`, `pattern-performance-tuning`, `technique-full-dp`