---
id: technique-pr-sgl-kernel-npu-79
title: "PR Insight: sgl-project/sgl-kernel-npu #79"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla-preprocess
  - kv-cache
  - nz-format
  - bf16
  - format-support
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/79"
---

# PR Insight: sgl-project/sgl-kernel-npu #79

**Title:** mlapo support bf16 KV Cache NZ format

## Overview
This PR adds BF16 KV Cache NZ format support to the MLA preprocessing operator. Updates mla_preprocess kernel implementation to handle NZ-formatted BF16 KV cache data efficiently on Ascend hardware.

## Technical Significance
Enables efficient KV cache storage using NZ format for BF16 precision, reducing memory footprint while maintaining performance. NZ format is Ascend's native memory layout that optimizes memory access patterns for the cube unit, particularly beneficial for KV cache in attention mechanisms.

## Related
- technique-mla
- technique-kv-cache
- technique-nz-format
- technique-bf16