---
id: technique-pr-vllm-ascend-8289
title: "PR Insight: vllm-project/vllm-ascend #8289"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - graph-capture
  - memory-planning
  - oom
  - profiling
  - configuration
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8289"
---

# PR Insight: vllm-project/vllm-ascend #8289

**Title:** [Feature] Account for Graph Capture Memory in KV Cache Planning

## Overview
This PR fixes KV cache memory planning by accounting for NPU graph capture memory consumption. Previously, NPUWorker computed available KV cache memory without considering graph capture memory, causing silent competition between graph capture and KV cache for the same gpu_memory_utilization budget. The solution tracks peak_activation_memory and non_torch_memory separately during profiling and outputs suggested kv-cache-memory values.

## Technical Significance
This fix prevents unexpected OOM errors and enables accurate KV cache sizing by properly accounting for all memory consumers. The ability to output suggested kv-cache-memory values allows users to skip profiling on future runs, improving startup time. The PR addresses a critical memory management issue that affected deployment reliability and performance predictability.

## Related
- `technique-kv-cache-optimization`
- `technique-memory-planning`
- `technique-graph-mode`