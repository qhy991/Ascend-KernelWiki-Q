---
id: technique-pr-vllm-ascend-2571
title: "PR Insight: vllm-project/vllm-ascend #2571"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rotary-embedding
  - rope
  - qwen
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2571"
---

# PR Insight: vllm-project/vllm-ascend #2571

**Title:** [main] Optimize rope in Qwen Models

## Overview
This PR optimizes rotary position embedding (RoPE) implementation in Qwen models. The changes improve rotary_embedding.py operations, update Qwen3 MoE model integration, and enhance test coverage for rotary embedding functionality.

## Technical Significance
The optimization improves RoPE computation efficiency for Qwen models on Ascend NPUs. By refining the rotary embedding implementation and updating the ascend_forward_context, the PR enables better performance for position-sensitive operations in transformer models. The changes also improve test coverage and validation of rotary embedding correctness.

## Related
- `technique-rotary-embedding`
- `technique-rope`
- `technique-qwen`