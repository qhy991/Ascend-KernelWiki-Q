---
id: technique-pr-vllm-ascend-2787
title: "PR Insight: vllm-project/vllm-ascend #2787"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - torchair
  - cache-hit
  - qwen
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2787"
---

# PR Insight: vllm-project/vllm-ascend #2787

**Title:** fix qwen torchair attention PrefillCacheHit

## Overview
This PR fixes a bug in the Qwen torchair attention implementation related to PrefillCacheHit handling. The change modifies the attention kernel in `vllm_ascend/torchair/torchair_attention.py` to correctly handle cache hit scenarios during prefill phase for Qwen models using torchair backend.

## Technical Significance
Fixes incorrect behavior in the attention mechanism when cache hits occur during prefill, which is critical for inference efficiency and correctness. The fix ensures that the torchair attention kernel properly manages the PrefillCacheHit state, preventing potential incorrect attention computations or memory access issues in Qwen models running with torchair backend.

## Related
- `kernel-attention-ascendc`, `technique-caching`, `technique-attention-optimization`