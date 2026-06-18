---
id: technique-pr-sgl-kernel-npu-284
title: "PR Insight: sgl-project/sgl-kernel-npu #284"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - optimization
  - sgemmv
  - refactoring
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/284"
---

# PR Insight: sgl-project/sgl-kernel-npu #284

**Title:** LoRA: Optimization LoRA kernels and refactoring

## Overview
Optimizes LoRA kernels and refactors the implementation to use SGLang's approach for LoRA adapter memory management instead of the vLLM-Ascend approach. Implements new sgemmv_expand and sgemmv_shrink kernels for improved performance and compatibility.

## Technical Significance
The refactoring aligns LoRA implementations with SGLang's memory management approach, reducing memory overhead and improving compatibility. The optimized sgemmv kernels provide better performance for LoRA operations, which are critical for efficient fine-tuning and inference with adapter-based models.

## Related
- `wiki-technique-lora`
- `wiki-kernel-matmul`
- `wiki-technique-memory-management`
- `wiki-technique-refactoring`