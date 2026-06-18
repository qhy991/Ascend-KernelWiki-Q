---
id: technique-pr-vllm-ascend-9282
title: "PR Insight: vllm-project/vllm-ascend #9282"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gdn
  - kv-cache
  - ascendc
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9282"
---

# PR Insight: vllm-project/vllm-ascend #9282

**Title:** [Feature] chunk_gated_delta_rule_fwd_h supports kvcache discontinuous…

## Overview
This PR adds support for discontinuous KV cache in the chunk_gated_delta_rule_fwd_h operator, which is part of the GDN (Gated Delta Network) implementation. The changes include updates to the operator definition, tiling logic, and GEMM kernel implementation to handle non-contiguous KV cache layouts.

## Technical Significance
Supporting discontinuous KV cache enables more efficient memory management and flexible caching strategies, which is important for models with variable-length sequences or complex attention patterns. This feature improves memory utilization and can reduce the overhead of KV cache management in certain scenarios.

## Related
- `hw-cube-unit`
- `kernel-attention`