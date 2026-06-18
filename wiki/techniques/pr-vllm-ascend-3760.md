---
id: technique-pr-vllm-ascend-3760
title: "PR Insight: vllm-project/vllm-ascend #3760"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hybridkv
  - kv-cache
  - memory-optimization
  - qwen3
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3760"
---

# PR Insight: vllm-project/vllm-ascend #3760

**Title:** [HybridKV][Bugfix] Fix Hybrid kvcache sharing bug in same attention type

## Overview
This PR fixes a HybridKV cache sharing bug where the same attention spec wasn't sharing buffers correctly, causing excessive HBM allocation. The fix modifies the `shared_by` logic in `vllm_ascend/worker/model_runner_v1.py` (24 additions, 18 deletions), resulting in 50% KV cache memory savings for Qwen3-next and enabling `gpu_memory_utilization` of 0.8 on A2 64G with TP4.

## Technical Significance
HybridKV uses multiple attention types (linear, SFA) that should share caches when possible. The bug prevented sharing, wasting memory. Proper buffer sharing allows higher batch sizes or larger models on the same hardware. This fix is critical for cost-efficient deployment of models like Qwen3-Next that mix attention types.

## Related
- `technique-hybridkv`
- `technique-kv-cache`
- `technique-memory-optimization`