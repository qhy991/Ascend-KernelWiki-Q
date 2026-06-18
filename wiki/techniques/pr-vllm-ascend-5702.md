---
id: technique-pr-vllm-ascend-5702
title: "PR Insight: vllm-project/vllm-ascend #5702"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - sharded-cp
  - all-gather
  - all-to-all
  - reduce-scatter
  - matmul
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5702"
---

# PR Insight: vllm-project/vllm-ascend #5702

**Title:** [Feature] Support DSA-CP for Hybrid scenario

## Overview
This PR extends DSA-CP (Decoupled Sharding Architecture with Context Parallel) to support the FULL_DECODE_ONLY execution mode in prefill-decode mixed serving scenarios. It modifies the weight distribution strategy for `q_proj` and `o_proj` operations, implementing different sharding schemes for pure prefill nodes versus hybrid nodes that handle both prefill and decode. The solution introduces additional collective operations (all_gather, all_to_all, reduce_scatter) during decode to enable sequence-parallel output aggregation while maintaining correctness under SFA CP.

## Technical Significance
This optimization improves throughput and resource utilization for decode-intensive workloads in mixed prefill-decode scenarios by enabling dynamic weight sharding strategies. The key technique is adding all_to_all before o_proj and reduce_scatter after o_proj during the decode graph replay phase to properly aggregate outputs across sequence-parallel groups. The benchmarks show significant improvements: TTFT increased by 527% and TPOT increased by 180%, demonstrating the effectiveness of adaptive sharding for heterogeneous execution patterns.

## Related
- `technique-hccl-optimization`, `technique-pipeline-scheduling`, `technique-all-gather`, `technique-reduce-scatter`, `technique-all-to-all`