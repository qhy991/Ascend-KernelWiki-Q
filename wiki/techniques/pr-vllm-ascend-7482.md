---
id: technique-pr-vllm-ascend-7482
title: "PR Insight: vllm-project/vllm-ascend #7482"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - qwen3.5
  - kernel-recompilation
  - constexpr
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7482"
---

# PR Insight: vllm-project/vllm-ascend #7482

**Title:** [Triton][Qwen3.5] delete expr for kernels args

## Overview
This PR removes unnecessary "constexpr" modifiers from Triton kernel parameters for Qwen3.5-related operators. The fix applies to chunk_o, l2norm, wy_fast, and layernorm_gated kernels to prevent unnecessary recompilation when parameters change.

## Technical Significance
This optimization matters for Qwen3.5 Triton kernel performance on Ascend. Qwen3.5 uses various specialized Triton kernels for attention and normalization operations. Removing constexpr from parameters that vary at runtime eliminates recompilation overhead, improving inference efficiency for this model family.

## Related
- technique-triton
- technique-qwen3.5
- pattern-kernel-optimization