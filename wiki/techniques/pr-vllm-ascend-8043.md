---
id: technique-pr-vllm-ascend-8043
title: "PR Insight: vllm-project/vllm-ascend #8043"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - sfa
  - prefill-context-parallel
  - kv-cache
  - hccl
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8043"
---

# PR Insight: vllm-project/vllm-ascend #8043

**Title:** [Performance][SFA] Reduce prefill KV all-gather communication for PCP/DCP

## Overview
This PR optimizes SFA (Sliding Window Flash Attention) models with prefill context parallel (PCP) and decode context parallel (DCP) enabled. Previously, prefill performed full-KV all-gather to support graph mode, but SFA attention computation in prefill is not captured in graph mode. The implementation changes the prefill path in `vllm_ascend/attention/context_parallel/sfa_cp.py` to gather only the required KV instead of the full KV, significantly reducing communication overhead and improving TTFT.

## Technical Significance
The optimization dramatically reduces HCCL all-gather communication overhead by eliminating unnecessary KV cache transfers for prefill SFA attention. Since SFA prefill attention is not graph-captured, gathering the full KV is wasteful. The selective KV gathering ensures only the tokens needed for sliding window attention are communicated, directly improving TTFT for SFA models with context parallelism enabled on Ascend clusters.

## Related
- `kernel-attention` (SFA attention)
- `technique-context-parallel` (PCP/DCP)
- `technique-hccl-optimization` (KV cache communication)