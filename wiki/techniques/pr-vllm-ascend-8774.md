---
id: technique-pr-vllm-ascend-8774
title: "PR Insight: vllm-project/vllm-ascend #8774"
type: wiki-technique
architectures:
  - ascend310p
  - ascend910
  - ascend910b
tags:
  - vllm
  - mrope
  - rope
  - ascend310p
  - caching
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8774"
---

# PR Insight: vllm-project/vllm-ascend #8774

**Title:** [Performance][310P] Optimize M-RoPE with cache and NPU forward integration

## Overview
This PR optimizes M-RoPE (Multi-scale Rotary Position Embedding) for Ascend 310P by adding a caching path and NPU forward integration. Key changes include precomputing cos/sin slices once per forward pass with stable buffers for graph replay, creating `AscendMRotaryEmbedding310` that uses `npu_apply_rotary_pos_emb` for rotary_dim=64/128, integrating M-RoPE preparation into the 310P model forward pass, and registering the custom op for automatic replacement.

## Technical Significance
M-RoPE is an extension of RoPE that handles multi-scale position encoding, important for models like Qwen2.5 that use variable context lengths. The optimization reduces redundant computation by caching rotary embedding values and leverages the NPU's `npu_apply_rotary_pos_emb` operator for hardware acceleration when the rotary dimension matches supported values. This improves performance for M-RoPE models on 310P while maintaining correctness via PyTorch fallback for unsupported dimensions.

## Related
- `kernel-attention-ascendc`
- `technique-cube-vector-overlap`
- `hw-vector-unit`