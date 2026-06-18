---
id: technique-pr-vllm-ascend-6602
title: "PR Insight: vllm-project/vllm-ascend #6602"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rotary-embedding
  - rope
  - triton
  - fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6602"
---

# PR Insight: vllm-project/vllm-ascend #6602

**Title:** [v0.13.0][Ops] Make triton rope support index_selecting from cos_sin_cache

## Overview
This PR extends Triton RoPE implementations to support cos_sin_cache and positions as inputs, aligning with vLLM's RoPE API. The change updates rope_triton_forward and split_qkv_rmsnorm_rope operations, registering rope_forward_oot as a new custom operation for use in fused compilation passes.

## Technical Significance
Enables more flexible RoPE operations by avoiding pre-computation and allowing draft models to have different RoPE parameters than main models. This improves acceptance rate and accuracy in speculative decoding scenarios while maintaining performance through efficient direct memory access in Triton kernels.

## Related
- `kernel-attention`