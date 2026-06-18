---
id: technique-pr-sgl-kernel-npu-268
title: "PR Insight: sgl-project/sgl-kernel-npu #268"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fp8
  - soft-fp8
  - matmul
  - quantization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/268"
---

# PR Insight: sgl-project/sgl-kernel-npu #268

**Title:** add soft fp8 feat(matmul and grouped matmul ops)

## Overview
Implements soft FP8 support with software-based FP8 computation paths and weight dequantization (FP8 → BF16). Includes MatMul and Grouped MatMul operations with integrated weight dequantization, tested on Qwen3-MoE-30B-A3B-FP8 and DeepSeekR1-0528 models.

## Technical Significance
Soft FP8 enables memory and computation efficiency for large model inference without requiring hardware FP8 support. The software implementation with weight dequantization provides a practical path for FP8 deployment on existing Ascend hardware, significantly reducing memory bandwidth requirements while maintaining accuracy through careful dequantization strategies.

## Related
- `wiki-kernel-matmul`
- `wiki-technique-quantization`
- `wiki-technique-fp8`
- `wiki-technique-soft-computation`