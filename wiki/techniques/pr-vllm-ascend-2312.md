---
id: technique-pr-vllm-ascend-2312
title: "PR Insight: vllm-project/vllm-ascend #2312"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - torchair
  - caching
  - compilation
  - configuration
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2312"
---

# PR Insight: vllm-project/vllm-ascend #2312

**Title:** [v0.9.1][bugfix] fix torchair runtime errror caused by configuration mismtaches and .kv_cache_bytes file missing

## Overview
This PR fixes TorchAir runtime errors caused by configuration mismatches and missing `.kv_cache_bytes` files. Instead of forcing users to prepare everything before enabling `use_cached_npu_graph`, the system now compiles the graph twice (the second compilation being much faster) when caching is enabled. Changes affect `vllm_ascend/platform.py`, `vllm_ascend/worker/worker_v1.py`, and `vllm_ascend/worker/model_runner_v1.py`.

## Technical Significance
This fix improves user experience by making TorchAir graph caching more robust and easier to use. Users are recommended to enable both `use_cached_kv_cache_bytes` and `use_cached_graph` for maximum performance, but without the cache bytes file, the system gracefully falls back to compiling twice instead of failing with confusing runtime errors.

## Related
- `technique-torchair-integration`, `technique-graph-caching`, `technique-configuration-management`, `technique-robust-compilation`