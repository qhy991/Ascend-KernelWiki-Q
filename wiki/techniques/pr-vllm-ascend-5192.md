---
id: technique-pr-vllm-ascend-5192
title: "PR Insight: vllm-project/vllm-ascend #5192"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mla
  - memory-optimization
  - mlapo
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5192"
---

# PR Insight: vllm-project/vllm-ascend #5192

**Title:** [perf] Fix MLAPO weight disposal for KV-consumer MLA in PD-mix deploy...

## Overview
This PR fixes a memory optimization issue in MLA+MLAPO deployments where KV-consumer nodes unnecessarily kept fused_qkv_a_proj/q_proj weights and quant parameters. The fix conditionally drops these tensors when `kv_transfer_config.is_kv_consumer` to reclaim memory.

## Technical Significance
MLAPO (MLA Pre-only) uses prepacked buffers for KV computation, making original weight tensors unnecessary on decode nodes. Dropping them reduces memory footprint in PD-mix (Prefill-Decode mixed) deployments, enabling larger batch sizes or more efficient resource utilization on Ascend NPUs.

## Related
- technique-mla
- technique-kv-cache-paging
- technique-memory-optimization