---
id: technique-pr-vllm-ascend-3738
title: "PR Insight: vllm-project/vllm-ascend #3738"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - all2allv
  - token-permute
  - hccl-optimization
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3738"
---

# PR Insight: vllm-project/vllm-ascend #3738

**Title:** [Perf] [MoE] optimize all2allv

## Overview
This PR optimizes MoE (Mixture of Experts) all2allv communication by replacing `init_routing_v2` with `token_permute` to improve performance. The change to `vllm_ascend/ops/fused_moe/token_dispatcher.py` removes 22 lines and adds 5 lines. Benchmark results show throughput improvement for bs=48, rr=10000, 2k input to 20k output scenarios.

## Technical Significance
All2allv is the communication pattern used in MoE to route tokens to expert nodes and gather results. Optimizing this operation with `token_permute` reduces communication overhead and improves overall MoE throughput. This change requires CANN 8.3, indicating it leverages newer hardware features or kernel optimizations.

## Related
- `technique-moe`
- `technique-hccl-optimization`
- `technique-all2all`