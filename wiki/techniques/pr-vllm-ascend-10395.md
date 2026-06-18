---
id: technique-pr-vllm-ascend-10395
title: "PR Insight: vllm-project/vllm-ascend #10395"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - triton
  - rope
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10395"
---

# PR Insight: vllm-project/vllm-ascend #10395

**Title:** [Ascend950] [Bugfix] Fix triton kernel performance fluctuation issue for ascend950

## Overview
This PR fixes a Triton kernel performance fluctuation issue on Ascend 950 for Qwen3-32B and Qwen3-235B models. The `split_qkv_rmsnorm_rope_simt` kernel was always being recompiled when the batch size changed because the input parameter `N` of the `precompute_rope_cos_sin_kernel` was declared as `tl.constexpr`, making it a compile-time constant. This caused intolerable compilation overhead on batch size changes. The fix removes the `tl.constexpr` qualifier from parameter `N`, allowing it to be a runtime variable and eliminating the recompilation.

## Technical Significance
This fix addresses a critical performance issue where kernel recompilation was causing non-deterministic throughput and significant overhead. The use of `tl.constexpr` for batch-dependent parameters forces kernel recompilation on every batch size change, which is unacceptable in production. By making `N` a runtime parameter, the kernel can be reused across different batch sizes, providing stable performance. This demonstrates an important Triton optimization principle: avoid `tl.constexpr` for parameters that vary at runtime to prevent excessive recompilation.

## Related
- `technique-triton-optimization`
- `technique-rope`
- `hw-ascend950`