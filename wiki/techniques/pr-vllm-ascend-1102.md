---
id: technique-pr-vllm-ascend-1102
title: "PR Insight: vllm-project/vllm-ascend #1102"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - scheduler
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1102"
---

# PR Insight: vllm-project/vllm-ascend #1102

**Title:** [Misc] fix initialize_kv_cache

## Overview
This PR adapts upstream vLLM changes to the KV cache manager, specifically addressing changes introduced in vLLM commit `f8a1a2d108d290791ae1245b2ee309f38fdd7619`. The modifications ensure compatibility and maintain CI test stability across `vllm_ascend/core/scheduler.py`, `vllm_ascend/worker/model_runner_v1.py`, and related test files.

## Technical Significance
This PR maintains synchronization between vLLM-Ascend and upstream vLLM development, ensuring that KV cache initialization works correctly with the latest vLLM scheduler changes. By adapting the upstream modifications, it prevents CI failures and maintains proper KV cache management for Ascend inference.

## Related
- `technique-kv-cache`
- `technique-scheduler`