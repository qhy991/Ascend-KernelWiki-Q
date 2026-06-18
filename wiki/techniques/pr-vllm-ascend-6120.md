---
id: technique-pr-vllm-ascend-6120
title: "PR Insight: vllm-project/vllm-ascend #6120"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - dsa-cp
  - pd-mixed
  - communication
  - tp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6120"
---

# PR Insight: vllm-project/vllm-ascend #6120

**Title:** [v0.13.0][Feature] Support DSA-CP for Hybrid scenario (#5702)

## Overview
This PR extends DSA-CP (Dynamic Sequence-Aware Context Parallelism) to handle FULL_DECODE_ONLY execution mode in prefill-decode mixed serving environments. Key changes: q_proj is fully replicated on PD-mixed nodes to avoid decode communication overhead, while o_proj uses all_gather during prefill and all_to_all + reduce_scatter during decode for sequence-parallel output aggregation under SFA CP.

## Technical Significance
This optimization significantly improves throughput (TTFT +527%, TPOT +180%) for decode-intensive workloads by strategically avoiding all_gather operations during decode phases while maintaining correctness through additional communication patterns during graph replay. The hybrid approach balances prefill and decode performance requirements.

## Related
- `technique-hccl-optimization`, `technique-communication-patterns`, `technique-dsa-cp`