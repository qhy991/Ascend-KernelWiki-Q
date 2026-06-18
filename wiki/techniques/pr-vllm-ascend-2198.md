---
id: technique-pr-vllm-ascend-2198
title: "PR Insight: vllm-project/vllm-ascend #2198"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - parallel-strategies
  - shared-expert
  - communication-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2198"
---

# PR Insight: vllm-project/vllm-ascend #2198

**Title:** [main][prefill optimization] Optimize parallel strategies to reduce communication overhead

## Overview
This PR optimizes MoE parallel strategies by switching shared expert sharding from TP-aligned to pure DP, changing O_Proj AllReduce to ReduceScatter, and postponing AllGather until after QKV down projection. These changes reduce synchronization impact during prefill. The implementation modifies `vllm_ascend/models/deepseek_v2.py`, `vllm_ascend/attention/mla_v1.py`, and adds the `enable_shared_expert_dp` configuration option.

## Technical Significance
This optimization significantly reduces communication overhead during prefill by leveraging more efficient collective operations and better sharding strategies. Using ReduceScatter instead of AllReduce for O_Proj reduces communication volume, and delaying AllGather until after expensive computations improves overlap and reduces synchronization delays. The pure DP sharding for shared experts enables more efficient execution.

## Related
- `kernel-fused-moe-ascendc`, `kernel-mla-v1`, `technique-parallel-strategies`, `technique-hccl-optimization`