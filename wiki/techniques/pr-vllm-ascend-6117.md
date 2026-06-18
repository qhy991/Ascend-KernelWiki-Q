---
id: technique-pr-vllm-ascend-6117
title: "PR Insight: vllm-project/vllm-ascend #6117"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - refactoring
  - attention
  - layernorm
  - kv-cache
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6117"
---

# PR Insight: vllm-project/vllm-ascend #6117

**Title:** [Refact.]: refactoring for 310p kvcache and some ops class

## Overview
This PR refactors Ascend 310P-specific implementations to decouple them from the main branch. Key changes include: refactoring LayerNorm and activation operator classes, using `torch_npu._npu_flash_attention_unpad` for encoder attention, removing 16× alignment padding from QKV inputs in prefill stage, and aligning KV cache initialization logic with mainline implementation.

## Technical Significance
This refactoring improves maintainability by creating clean 310P-specific implementations while maintaining compatibility. The move to use `torch_npu._npu_flash_attention_unpad` leverages native NPU operators for better performance, and removing unnecessary padding reduces memory overhead and computation during prefill stages.

## Related
- `technique-flash-attention`, `technique-layernorm`, `technique-kv-cache-paging`, `kernel-attention-npu-op`