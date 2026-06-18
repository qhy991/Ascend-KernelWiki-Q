---
id: technique-pr-mindspeed-1478
title: "PR Insight: Ascend/MindSpeed #1478"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - attention
  - ulysses
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1478"
---

# PR Insight: Ascend/MindSpeed #1478

**Title:** ulycesss kv_head不够分的时候，进行repeat操作

## Overview
This PR adds repeat operations for Ulysses attention when KV heads cannot be evenly distributed. Ulysses is a sequence parallelism strategy for attention, and this fix handles cases where the number of KV heads doesn't divide evenly across parallel ranks.

## Technical Significance
Enables proper handling of Ulysses attention in cases where KV head count is not divisible by the number of parallel ranks. The repeat operation ensures correct attention computation while maintaining load balance across ranks.

## Related
- `kernel-attention`
- `technique-sequence-parallelism`