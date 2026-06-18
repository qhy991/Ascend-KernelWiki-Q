---
id: technique-pr-vllm-ascend-1395
title: "PR Insight: vllm-project/vllm-ascend #1395"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - allreduce
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1395"
---

# PR Insight: vllm-project/vllm-ascend #1395

**Title:** shared_experts+router_experts merge all_reduce(Improve TTOP 5ms)

## Overview
This PR merges all-reduce operations for shared experts and router experts in MoE inference, reducing communication overhead and improving time-to-output (TTOP) by 5ms.

## Technical Significance
Optimizes MoE communication by fusing separate all-reduce operations for shared and routed experts into a single collective operation. This reduces synchronization overhead and improves bandwidth utilization, which is critical for distributed MoE inference where communication dominates latency.

## Related
- `kernel-moe`
- `technique-hccl-optimization`
- `technique-operator-fusion`