---
id: technique-pr-vllm-ascend-10202
title: 'PR Insight: vllm-project/vllm-ascend #10202'
type: wiki-technique
architectures:
- ascend910
- ascend910b
tags:
- pipeline-parallel
- kv-cache
- communication
confidence: inferred
sources:
- pr-vllm-ascend-10202
---

# PR Insight: vllm-project/vllm-ascend #10202

**Title:** [BugFix] Fix layer index mapping and block ID flattening in Mooncake connector

## Overview
This PR fixes a KV transfer failure in the Mooncake connector under Pipeline Parallel (PP) configurations. The root cause was that `self.total_layers` was initialized via `get_num_layers()` which returns per-stage layer count (divided by PP rank), but `extract_layer_index()` returns global layer numbers. For example, with a 48-layer model and PP=2, each stage sees `total_layers=24`, but PP rank 1 holds layers 24–47. This caused MTP virtual-layer indices to collide with actual base-layer indices, corrupting KV cache metadata and producing incorrect KV transfers in P/D scenarios.

## Technical Significance
This is a critical distributed correctness fix for PP+MTP scenarios. The issue demonstrates the complexity of layer index management in pipeline parallel environments where different stages hold disjoint layer ranges. The fix ensures that MTP virtual-layer indices always start above all base-layer indices by using `get_total_num_hidden_layers()` to obtain the global layer count. Additionally, it fixes block invalidation logic to only invalidate blocks in the full-attention group, preventing incorrect KV cache metadata propagation.

## Related
- `technique-pipeline-parallel`
- `technique-kv-cache-paging`
- `technique-mtp`