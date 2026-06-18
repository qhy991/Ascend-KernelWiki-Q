---
id: technique-pr-modellink-2674
title: "PR Insight: Ascend/ModelLink #2674"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qlora
  - feature
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2674"
---

# PR Insight: Ascend/ModelLink #2674

**Title:** [feat] QLoRA GMM Support

## Overview
This PR adds support for Generalized Matrix Multiplication (GMM) operations in QLoRA training. QLoRA is an efficient fine-tuning technique that quantizes model weights to 4-bit while training with full precision. GMM support enables more efficient matrix operations during the fine-tuning process.

## Technical Significance
QLoRA with GMM support significantly improves the efficiency of large model fine-tuning on Ascend hardware. Optimized matrix operations reduce memory bandwidth and improve training throughput, making it practical to fine-tune large models on Ascend NPUs with limited memory.

## Related
- technique-matmul
- technique-gemm