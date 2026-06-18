---
id: technique-pr-vllm-ascend-3074
title: "PR Insight: vllm-project/vllm-ascend #3074"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek
  - mtp
  - shared-expert
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3074"
---

# PR Insight: vllm-project/vllm-ascend #3074

**Title:** [misc][torchair] fix bugs around `deepseek mtp`, `enable_shared_expert_dp` and `use_cached_kv_cache_bytes`

## Overview
This PR contains multiple bug fixes: 1) DeepseekMTPLayer initialization and forward bugs with shared_expert_dp enabled, 2) tensor shape mismatches after o_proj due to NPUModelRunner workaround, 3) unnecessary KV cache memory decline with use_cached_kv_cache_bytes disabled, 4) Fallback from MC2 to All2All due to mc2_mask padding incompatibility.

## Technical Significance
The fixes address correctness and performance issues across multiple features: shared expert DP, MTP layers, KV cache management, and communication methods. Proper handling of tensor shapes and memory allocation is critical for correctness and performance in complex model architectures.

## Related
- `kernel-deepseek-ascendc`, `technique-shared-expert-dp`, `kernel-moe-ascendc`