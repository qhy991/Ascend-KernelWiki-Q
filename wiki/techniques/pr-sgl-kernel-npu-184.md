---
id: technique-pr-sgl-kernel-npu-184
title: "PR Insight: sgl-project/sgl-kernel-npu #184"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - decode
  - triton
  - kernels
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/184"
---

# PR Insight: sgl-project/sgl-kernel-npu #184

**Title:** Add triton decode attention kernels

## Overview
Implements Triton-based decode attention kernels for Ascend NPU, along with comprehensive test scripts. The kernels provide optimized attention computation for the decode phase of autoregressive language model inference.

## Technical Significance
Decode attention is a critical bottleneck in LLM inference, and Triton kernels provide highly optimized implementations for Ascend architecture. The comprehensive test suite ensures correctness and performance validation. These kernels directly impact inference latency and throughput for decode-phase operations in LLM serving.

## Related
- `wiki-kernel-attention`
- `wiki-technique-decode-optimization`
- `wiki-language-triton`
- `wiki-kernel-flash-attention`