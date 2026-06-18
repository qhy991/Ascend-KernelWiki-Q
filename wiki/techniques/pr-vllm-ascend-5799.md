---
id: technique-pr-vllm-ascend-5799
title: "PR Insight: vllm-project/vllm-ascend #5799"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - rotary-embedding
  - qk-split
  - torch-npu
  - performance
  - elementwise
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5799"
---

# PR Insight: vllm-project/vllm-ascend #5799

**Title:** [MM][Perf] Merge Q/K split to simplify AscendApplyRotaryEmb for better performance

## Overview
This PR optimizes the rotary embedding implementation by merging Q/K split operations and using upstream utility functions to reduce code redundancy. The implementation refactors `vllm_ascend/ops/rotary_embedding.py` to use upstream `_pre_process()` and `_post_process()` utility functions, and merges the Q/K split logic to simplify calls to `torch_npu.npu_rotary_mul()`. The optimization reduces redundant code and improves performance by minimizing the number of operator calls.

## Technical Significance
This performance optimization reduces TPOT (Time Per Output Token) by 6.22% through code simplification and reduced operator overhead. The key technique is merging Q/K split operations to minimize calls to the NPU rotary multiplication operator, which reduces kernel launch overhead and improves efficiency. By leveraging upstream utility functions, the code is also more maintainable and consistent with the main vLLM codebase. Benchmarks on Qwen2.5-VL-7B-Instruct show improved throughput: request throughput increased from 1.68 to 1.75 req/s, output token throughput from 167.05 to 174.45 tok/s, and peak output token throughput from 261.00 to 279.00 tok/s.

## Related
- `technique-rotary-embedding`, `technique-elementwise`, `technique-performance-optimization`, `technique-operator-fusion`