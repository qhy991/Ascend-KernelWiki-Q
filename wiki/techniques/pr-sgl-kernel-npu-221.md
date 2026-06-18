---
id: technique-pr-sgl-kernel-npu-221
title: "PR Insight: sgl-project/sgl-kernel-npu #221"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dispatch
  - prefix-sum
  - configuration
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/221"
---

# PR Insight: sgl-project/sgl-kernel-npu #221

**Title:** normal_dispatch num_recv_tokens_per_expert_list support prefixSum

## Overview
Adds prefix sum support for num_recv_tokens_per_expert_list in normal dispatch operations. Controlled by environment variable MOE_EXPERT_TOKEN_NUMS_TYPE: 0 for prefix sum, 1 for token counts (default).

## Technical Significance
Prefix sum representation enables more efficient downstream processing for some MoE implementations, as it provides cumulative token counts that can be used directly for indexing operations. The configurable approach allows compatibility with different framework expectations while maintaining backward compatibility with the default token count format.

## Related
- `wiki-kernel-moe`
- `wiki-technique-prefix-sum`
- `wiki-technique-configuration`
- `wiki-technique-data-format`