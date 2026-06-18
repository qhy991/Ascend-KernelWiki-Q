---
id: technique-pr-vllm-ascend-6964
title: "PR Insight: vllm-project/vllm-ascend #6964"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - static-kernels
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6964"
---

# PR Insight: vllm-project/vllm-ascend #6964

**Title:** [Bugfix] Fix the moe_forward error when setting enable_static_kernel …

## Overview
Fixes MoE forward pass errors when `enable_static_kernel` is set to true. When static kernels are enabled, the forward pass runs twice (compilation + capture), causing `moe_layer_index` to overflow. The fix wraps the index to prevent out-of-bounds errors.

## Technical Significance
Prevents memory access violations in MoE forward pass when using static kernel compilation. The index wrapping ensures correct layer indexing across compilation and capture phases, maintaining stability with static kernel optimization.

## Related
- `technique-moe`, `technique-static-kernels`, `technique-compilation`