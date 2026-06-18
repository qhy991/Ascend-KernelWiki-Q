---
id: technique-pr-vllm-ascend-8050
title: "PR Insight: vllm-project/vllm-ascend #8050"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - sfa
  - kv-cache
  - hccl
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8050"
---

# PR Insight: vllm-project/vllm-ascend #8050

**Title:** [Performance] Optimize KV cache gathering by selecting blocks before all-gather

## Overview
This PR optimizes KV cache gathering in `vllm_ascend/attention/context_parallel/sfa_cp.py` by first selecting only the KV cache blocks referenced by the current batch's block_tables using `torch.index_select`, then performing the all-gather only on this reduced set. Previously, the implementation performed all-gather on the entire KV cache, including unused blocks.

## Technical Significance
The optimization dramatically reduces HCCL all-gather communication volume for context parallel SFA inference. Benchmarks on 64k input show TTFT improvement from 728.66s to 398.31s (45% improvement) and TPOT improvement from 2.07s to 0.21s (90% improvement). This is achieved by eliminating unnecessary data transfers of unused KV blocks, directly impacting both latency and throughput for long-context models on Ascend clusters.

## Related
- `kernel-attention` (SFA attention with KV cache)
- `technique-context-parallel` (KV cache distribution)
- `technique-hccl-optimization` (Communication optimization)