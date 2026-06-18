---
id: technique-pr-vllm-ascend-4788
title: "PR Insight: vllm-project/vllm-ascend #4788"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - qwen3-next
  - gateddeltanet
  - qkv-zba
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4788"
---

# PR Insight: vllm-project/vllm-ascend #4788

**Title:** qwen3_next add triton ops : fused_qkvzba_split_reshape

## Overview
This PR adds a new Triton operator `fused_qkvzba_split_reshape_cat` for Qwen3-Next GatedDeltaNet models. The operator fuses QKV processing, zero-bit activation (ZBA) handling, and reshape/cat operations into a single kernel.

## Technical Significance
Provides a fused Triton kernel for Qwen3-Next's GatedDeltaNet architecture, combining multiple tensor operations (QKV split, ZBA handling, reshape, concatenation) to reduce kernel launch overhead and improve memory access patterns.

## Related
- `kernel-fused-qkvzba-split-reshape`
- `kernel-qwen3-next`
- `kernel-gateddeltanet`
- `technique-triton-optimization`
- `technique-operator-fusion`