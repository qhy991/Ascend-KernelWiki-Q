---
id: technique-pr-vllm-ascend-5701
title: "PR Insight: vllm-project/vllm-ascend #5701"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sfa
  - sharded-cp
  - comm-overlap
  - compute-comm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5701"
---

# PR Insight: vllm-project/vllm-ascend #5701

**Title:** [Perf] Supports compute-communication overlap in the forward of sfa_v1 in the Sharded-CP feature.

## Overview
This PR enables compute-communication overlap in the SFA v1 forward pass for the Sharded-CP feature, improving performance by hiding communication latency behind computation. The implementation affects SFA v1 attention and distributed utilities.

## Technical Significance
Performance optimization through compute-communication overlap, which is critical for reducing communication bottlenecks in multi-card inference. By overlapping allgather KV cache communication with computation, this PR improves throughput and reduces latency for Sharded-CP workloads, especially for long sequences.

## Related
- `kernel-attention-ascendc`, `technique-sfa`, `technique-compute-comm-overlap`