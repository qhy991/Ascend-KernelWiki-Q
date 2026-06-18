---
id: technique-pr-cann-ops-adv-5
title: "PR Insight: cann-ops-adv #5"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - flash-attention
  - operator-fusion
  - attention
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/5"
---

# PR Insight: cann-ops-adv #5 - Add ffn & IncreFlashAttention & PromptFlashAttention & FusedInferAttentionScore

## Overview
This PR adds multiple advanced operators: FFN (Feed-Forward Network), IncreFlashAttention (Incremental Flash Attention), PromptFlashAttention, and FusedInferAttentionScore. These operators implement key components of transformer architectures for efficient LLM inference on Ascend NPUs.

## Technical Significance
These additions expand the ops-adv library with optimized implementations of transformer primitives. The attention variants (IncreFlashAttention, PromptFlashAttention) support different inference scenarios like KV-cache reuse and prompt processing, while FusedInferAttentionScore fuses multiple operations to reduce kernel launch overhead. The FFN operator provides optimized MLP computation. Together they enable end-to-end efficient transformer inference.

## Related
- `kernel-flash-attention`
- `technique-operator-fusion`
- `kernel-attention`
- `technique-cube-vector-overlap`