---
id: technique-pr-sgl-kernel-npu-128
title: "PR Insight: sgl-project/sgl-kernel-npu #128"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - matmul
  - ascendc
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/128"
---

# PR Insight: sgl-project/sgl-kernel-npu #128

**Title:** LoRA: moving kernels from vllm-ascend repo

## Overview
This PR moves LoRA (Low-Rank Adaptation) kernels from the vllm-ascend repository to sgl-kernel-npu, consolidating LoRA inference support. It includes BGMV/SGMV expand and shrink kernels for efficient LoRA parameter application.

## Technical Significance
LoRA kernels enable efficient fine-tuning and inference by applying low-rank weight updates without full model retraining. The consolidation into sgl-kernel-npu centralizes kernel development and enables reuse across different frameworks (vLLM, sglang).

## Related
- `kernel-matmul-ascendc`, `technique-lora`