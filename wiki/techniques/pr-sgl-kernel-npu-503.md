---
id: technique-pr-sgl-kernel-npu-503
title: "PR Insight: sgl-project/sgl-kernel-npu #503"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mrope
  - rope
  - elementwise
  - ascendc
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/503"
---

# PR Insight: sgl-project/sgl-kernel-npu #503

**Title:** Add interleave mode for split qkv norm rope

## Overview
This PR adds support for interleaved rotary position embedding (RoPE) mode to the split QKV RMSNorm RoPE operator. The interleaved mode uses interleaved data layout to compute RoPE transformations, aligning with different scenes of mrope (multi-dimensional RoPE) including both interleaved and half formats. The implementation modifies the `split_qkv_rmsnorm_rope.py` file to support this additional data layout variant.

## Technical Significance
Adding interleaved RoPE support improves the operator's compatibility with different RoPE implementations and data formats used in transformer models. This is particularly important for supporting models that require interleaved data layouts for optimal performance or compliance with specific RoPE implementations. The enhancement expands the operator's versatility for various transformer architectures and ensures alignment with Ascend's mrope API capabilities.

## Related
- `technique-rope`
- `technique-rmsnorm`
- `kernel-attention`
- `pattern-data-layout`