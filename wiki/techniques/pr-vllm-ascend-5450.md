---
id: technique-pr-vllm-ascend-5450
title: "PR Insight: vllm-project/vllm-ascend #5450"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - rope
  - kernel-optimization
  - eagle
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5450"
---

# PR Insight: vllm-project/vllm-ascend #5450

**Title:** [Main][Ops] Make triton rope support index_selecting from cos_sin_cache

## Overview
This PR refactors Rotary Positional Embedding (RoPE) implementations in vllm-ascend to support index-based selection from a unified cos_sin_cache rather than pre-computed separate cos and sin tensors. It updates Triton kernels including `split_qkv_rmsnorm_rope_kernel` and `_triton_rope`, registers a new custom operation `rope_forward_oot`, and modifies the forward pass to accept unified cache and positions arguments.

## Technical Significance
This change improves RoPE flexibility for draft/Main model scenarios (like Eagle3) by enabling different RoPE parameters between models, and reduces memory operations by converting index_select/chunk operations to direct memory access in Triton kernels. The unified cache approach eliminates redundant pre-computation codes while maintaining performance accuracy for models like Qwen3-235b.

## Related
- `technique-operator-fusion` (QK-Norm-RoPE fusion pattern)
- `kernel-attention` (RoPE integration with attention kernels)
- `technique-triton` (Triton kernel optimization)