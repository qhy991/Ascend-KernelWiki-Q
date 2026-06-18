---
id: technique-pr-vllm-ascend-5477
title: "PR Insight: vllm-project/vllm-ascend #5477"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - fullgraph
  - qwen3
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5477"
---

# PR Insight: vllm-project/vllm-ascend #5477

**Title:** [Feat][main] Supported to use full-graph with Qwen3-Next-MTP

## Overview
This PR enables fullgraph compilation support for Qwen3-Next models using MTP (Multi-Token Prediction) speculative decoding. The implementation adapts `AscendAttentionState.ChunkedPrefill` in both the main model and MTP model to work with fullgraph compilation mode.

## Technical Significance
Combining MTP speculative decoding with fullgraph compilation for Qwen3-Next models provides significant performance benefits by reducing kernel launch overhead and enabling better operator fusion on Ascend NPU. The adaptation of chunked prefill attention states ensures compatibility between the graph compilation system and the MTP speculation mechanism.

## Related
- `technique-speculative-decoding` (MTP algorithm)
- `technique-fullgraph` (Graph compilation optimization)
- `kernel-attention` (ChunkedPrefill attention)
- `technique-qwen` (Qwen model family support)