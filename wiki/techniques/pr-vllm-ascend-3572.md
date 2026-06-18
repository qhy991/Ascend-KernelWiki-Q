---
id: technique-pr-vllm-ascend-3572
title: "PR Insight: vllm-project/vllm-ascend #3572"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - slot-mapping
  - qwen3
  - linear-attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3572"
---

# PR Insight: vllm-project/vllm-ascend #3572

**Title:** [Bugfix] Fix zero attention output in qwen3-next

## Overview
This PR fixes a critical bug where attention output was all zeros in Qwen3-next models. The issue occurred because Attention and LinearAttention shared the same `slot_mapping`, but LinearAttention's mapping was all zeros, overwriting the correct Attention mapping. The fix removes the unified `self.slot_mapping` and directly passes slot_mapping from `input_batch.blocktable` to `attn_metadata`, with block_table.slot_mapping set to int32.

## Technical Significance
Slot mapping determines which KV cache blocks each token uses for attention computation. The bug shows that incorrect slot mapping can completely invalidate attention outputs. The fix introduces proper data separation between different attention types and ensures correct data types for hardware compatibility. This is fundamental to correct KV cache management in spec decode scenarios.

## Related
- `technique-attention`
- `technique-kv-cache`
- `technique-spec-decode`