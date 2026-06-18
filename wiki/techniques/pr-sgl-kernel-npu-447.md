---
id: technique-pr-sgl-kernel-npu-447
title: "PR Insight: sgl-project/sgl-kernel-npu #447"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qkv-fusion
  - qwen3-next
  - performance-optimization
  - memory-layout
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/447"
---

# PR Insight: sgl-project/sgl-kernel-npu #447

**Title:** add fused_qkvzba_split_reshape_cat_contiguous_kernel

## Overview
This PR adds a fused_qkvzba_split_reshape_cat_contiguous_kernel that supports sequence lengths > 65536, significantly enhancing performance from 25μs to 12μs per operation for 64 batch size * 6144 dimension shapes. The kernel enables major performance improvements during prefill, especially for large batch sizes like 31480.

## Technical Significance
Supporting sequence lengths beyond 65536 enables processing of very long contexts required by modern LLMs. The performance optimization through contiguous memory layout and fusion provides substantial speedup for large-batch prefill scenarios, which are critical for efficient processing of long prompts.

## Related
- `kernel-qkv-fusion`, `kernel-reshape`, `kernel-concatenate`, `technique-memory-layout-optimization`