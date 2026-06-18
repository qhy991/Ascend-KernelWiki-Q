---
id: technique-pr-cann-ops-adv-13
title: "PR Insight: cann-ops-adv #13"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - flash-attention
  - attention
  - ascendc
  - parameter-updates
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/13"
---

# PR Insight: cann-ops-adv #13 - Update FA/FAG preTokens params

## Overview
This PR updates the preTokens parameters for FA (FlashAttention) and FAG (FlashAttentionScoreGrad) operators. The preTokens parameter typically controls how many previous tokens to attend to in incremental attention scenarios.

## Technical Significance
PreTokens parameters are critical for incremental/paged attention implementations used in LLM inference. The update improves parameter handling, likely supporting more flexible KV-cache usage patterns or fixing edge cases in the attention computation. This enables more efficient memory reuse during generation.

## Related
- `kernel-flash-attention`
- `technique-kv-cache-paging`
- `kernel-attention`
- `kernel-quant-matmul`