---
id: technique-pr-vllm-ascend-6827
title: "PR Insight: vllm-project/vllm-ascend #6827"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - split-qkv-rmsnorm-rope
  - triton
  - prefill
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6827"
---

# PR Insight: vllm-project/vllm-ascend #6827

**Title:** [Ops][Misc] Optimize split_qkv_rmsnorm_rope op

## Overview
This PR optimizes the split_qkv_rmsnorm_rope operator by adding a prefill-specific kernel for large batch sizes. The implementation dynamically selects between decode and prefill kernels based on batch size and adds support for partial rotation dimensions.

## Technical Significance
Improves performance for large batch prefill scenarios through optimized kernel selection. The prefill kernel handles batch sizes exceeding vector core availability more efficiently, while partial RoPE support provides greater flexibility.

## Related
- `kernel-attention`
- `technique-operator-fusion`