---
id: technique-pr-vllm-ascend-3184
title: "PR Insight: vllm-project/vllm-ascend #3184"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dummy-run
  - load-balance
  - token-distribution
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3184"
---

# PR Insight: vllm-project/vllm-ascend #3184

**Title:** [Feat] Load balance of tokens across experts in dummy_run

## Overview
This PR improves token load balancing during dummy_run by changing topk_ids from all zeros to random values. The previous implementation caused most tokens to accumulate on DP0TP0, leading to insufficient KV cache availability due to special input data characteristics.

## Technical Significance
Dummy_run is used for memory profiling and operator compilation. Balanced token distribution ensures accurate profiling and prevents artificial KV cache exhaustion on specific ranks. Random topk_ids provides better simulation of real token routing patterns, improving the reliability of dummy_run results.

## Related
- `kernel-moe-ascendc`, `technique-load-balance`, `pattern-dummy-run-optimization`