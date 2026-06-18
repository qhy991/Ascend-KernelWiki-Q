---
id: technique-pr-mindspeed-1861
title: "PR Insight: Ascend/MindSpeed #1861"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - attention
  - flash-attention
  - kv-cache
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1861"
---

# PR Insight: Ascend/MindSpeed #1861

**Title:** FA/FAG支持KVDim不等长

## Overview
This PR adds support for unequal KV dimension lengths in FA (Flash Attention) and FAG (likely Flash Attention with Grouped Query Attention). This enables handling of variable-length key-value cache dimensions.

## Technical Significance
Unequal KV dimensions are important for flexible attention patterns and grouped-query attention variants. Supporting this in flash attention enables more efficient memory usage and better handling of non-standard attention configurations on Ascend NPUs.

## Related
- flash-attention
- grouped-query-attention
- kv-cache management