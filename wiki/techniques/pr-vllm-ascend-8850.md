---
id: technique-pr-vllm-ascend-8850
title: "PR Insight: vllm-project/vllm-ascend #8850"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mooncake-connector
  - kv-cache
  - hybrid-attention
  - distributed
  - pipeline-decoding
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8850"
---

# PR Insight: vllm-project/vllm-ascend #8850

**Title:** [Feature] [P/D] support hybrid attention for mooncake connector

## Overview
This PR adapts MooncakeConnector KV transfer metadata handling for hybrid KV cache layouts. The core change makes Mooncake KV transfer operate on KV-cache-group-aware metadata instead of assuming a single uniform attention-only KV layout. It builds per-group/per-layer metadata including `kv_group2layeridx`, `block_size_scale`, `block_len_per_addr`, and `kv_caches_base_addr`. This enables support for hybrid KV cache transfer paths while maintaining backward compatibility.

## Technical Significance
Hybrid attention combines different attention mechanisms (e.g., attention + Mamba) within a single model, requiring different KV cache layouts. The Mooncake connector handles distributed KV cache transfer in pipeline-decoding scenarios. This enhancement allows the connector to correctly transfer non-uniform KV cache groups, ensuring correct multi-node inference for models with hybrid attention patterns like BaLing. The metadata infrastructure enables precise control over which cache blocks are transferred between devices.

## Related
- `technique-kv-cache-paging`
- `technique-hccl-optimization`
- `technique-data-reuse`