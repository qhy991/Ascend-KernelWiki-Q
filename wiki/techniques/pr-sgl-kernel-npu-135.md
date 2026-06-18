---
id: technique-pr-sgl-kernel-npu-135
title: "PR Insight: sgl-project/sgl-kernel-npu #135"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mla
  - quantization
  - nz-format
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/135"
---

# PR Insight: sgl-project/sgl-kernel-npu #135

**Title:** support cachemode int8_nzcache with bf16 in mla_preprocess

## Overview
This PR adds a new execution path in the MLA preprocess kernel to support cacheMode int8_nzcache with BF16 computation, enabling mixed-precision inference with INT8 cache storage.

## Technical Significance
Mixed-precision cache storage (INT8) with BF16 computation balances memory efficiency and accuracy. NZ format for cache leverages Ascend's optimized memory access patterns. This combination is critical for large models where KV cache dominates memory usage.

## Related
- `kernel-attention-ascendc`, `technique-quantization`, `hw-nz-format`