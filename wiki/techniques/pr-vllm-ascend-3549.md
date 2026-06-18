---
id: technique-pr-vllm-ascend-3549
title: "PR Insight: vllm-project/vllm-ascend #3549"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - layernorm
  - qwen3
  - kernel-bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3549"
---

# PR Insight: vllm-project/vllm-ascend #3549

**Title:** [BugFix][mian] Fixed a triton kernel bug of layer_norm_fwd_kernel for Qwen3-next

## Overview
This PR fixes a bug in the Triton kernel `layer_norm_fwd_kernel` that was causing an exception "coreDim=xxx can't be greater than UINT16_MAX" when KV cache usage reached 100%. The fix was applied to `vllm_ascend/ops/fla.py` and was tested with Qwen3-Next-80B-A3B-Instruct model under high-load scenarios with batch_size=512 and large max_out_len=30000.

## Technical Significance
The layer normalization kernel bug manifested under extreme memory pressure (100% KV cache usage) during large-batch inference. The fix ensures the Triton kernel correctly handles large core dimensions beyond UINT16_MAX, preventing crashes in production inference workloads with Qwen3 models. This is critical for stability of MTP (multi-text-prompt) inference with large token outputs.

## Related
- `technique-triton-kernel`
- `technique-layernorm`
- `technique-kv-cache-paging`