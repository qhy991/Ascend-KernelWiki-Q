---
id: technique-pr-vllm-ascend-4983
title: "PR Insight: vllm-project/vllm-ascend #4983"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - allreduce
  - moe
  - mc2
  - kv-consumer
  - multi-node
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4983"
---

# PR Insight: vllm-project/vllm-ascend #4983

**Title:** [perf] replace all_reduce for kv_consumer and support different num_tokens among all ranks

## Overview
This PR eliminates the all_reduce operation for decode nodes in _sync_metadata_across_dp (which uses slow gloo backend across nodes) and modifies MoEDispatch & MoeCombine operator inputs to support MC2EP with different num_tokens across ranks. This addresses cross-node all_reduce bottlenecks in multi-node speculative decoding scenarios.

## Technical Significance
Reduces latency in multi-node PD disaggregation deployments by removing expensive cross-node all_reduce operations and enabling MC2EP to handle variable token counts per rank. Tested with 2P:DP2TP8EP16 (prefill) and DP8TP4EP32 (decode) with async scheduling.

## Related
- `kernel-allreduce`
- `kernel-moe-dispatch`
- `kernel-moe-combine`
- `kernel-mc2`
- `technique-multi-node-optimization`
- `technique-pd-disaggregation`