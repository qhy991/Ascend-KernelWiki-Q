---
id: technique-pr-sgl-kernel-npu-196
title: "PR Insight: sgl-project/sgl-kernel-npu #196"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - memory-allocation
  - long-sequence
  - overflow
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/196"
---

# PR Insight: sgl-project/sgl-kernel-npu #196

**Title:** Add alloc_extend_kernel

## Overview
Adds an Ascend-specific alloc_extend_kernel adapted from the community version, which fixes undefined behavior overflow exceptions when running long sequences on Ascend devices.

## Technical Significance
Long sequence inference is challenging due to memory allocation overflow issues. This Ascend-specific adaptation prevents UB overflow exceptions that occur with long sequences, enabling reliable long-context LLM inference. The fix is critical for production deployments requiring extended context lengths.

## Related
- `wiki-technique-memory-allocation`
- `wiki-technique-long-sequence`
- `wiki-technique-bugfix`
- `wiki-kernel-attention`