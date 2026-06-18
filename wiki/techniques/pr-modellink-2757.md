---
id: technique-pr-modellink-2757
title: "PR Insight: Ascend/ModelLink #2757"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - qlora
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2757"
---

# PR Insight: Ascend/ModelLink #2757

**Title:** fix bug when gemm and qlora in inference

## Overview
This PR fixes a bug that occurred when using GEMM operations with QLoRA (Quantized Low-Rank Adaptation) during inference. The fix resolves an incompatibility between the quantization scheme and matrix multiplication operations.

## Technical Significance
QLoRA is important for memory-efficient fine-tuning and inference. This bugfix ensures that quantized models can perform inference correctly on Ascend NPUs, leveraging the hardware's efficient support for quantized operations and GEMM computations.

## Related
- kernel-matmul
- technique-format-conversion