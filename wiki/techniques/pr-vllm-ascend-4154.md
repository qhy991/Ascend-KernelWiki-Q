---
id: technique-pr-vllm-ascend-4154
title: "PR Insight: vllm-project/vllm-ascend #4154"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sampling
  - topk-topp
  - performance
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4154"
---

# PR Insight: vllm-project/vllm-ascend #4154

**Title:** [perf][bugfix] improve performance of rejection sampler and eliminate HD synchronize in TopKTopPSampler

## Overview
This PR improves performance by: (1) Using optimized apply_top_k_top_p for NPU platform in rejection sampler to avoid scatter elements (~26ms TPOT reduction with bs=24 per DP), (2) Eliminating D2H synchronization before calling npu_top_k_top_p by dropping the fused operator (performance improvement not significant compared to async_scheduling and may bring accuracy issues), (3) Refactoring AscendTopKTopPSampler implementation to align with vLLM.

## Technical Significance
Eliminating scatter operations in rejection sampler provides significant TPOT improvement, which is critical for decode phase throughput. The refactoring aligns implementation with vLLM, improving maintainability. The decision to drop fused operator prioritizes correctness and async_scheduling compatibility over marginal performance gains.

## Related
- `technique-sampling`, `technique-topk-topp`, `pattern-performance-optimization`, `technique-synchronization`