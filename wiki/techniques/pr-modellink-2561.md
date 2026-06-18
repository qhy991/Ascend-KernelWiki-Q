---
id: technique-pr-modellink-2561
title: "PR Insight: Ascend/ModelLink #2561"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - feature
  - training
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2561"
---

# PR Insight: Ascend/ModelLink #2561

**Title:** gemm for lora

## Overview
This PR adds Generalized Matrix Multiplication (GEMM) optimizations for LoRA (Low-Rank Adaptation) training in ModelLink. The optimizations improve the efficiency of matrix operations during LoRA fine-tuning on Ascend hardware.

## Technical Significance
LoRA is an efficient fine-tuning technique that reduces memory and compute requirements. GEMM optimizations for LoRA improve training throughput and reduce memory bandwidth usage, making LoRA fine-tuning even more practical on Ascend NPUs for large language models.

## Related
- technique-matmul
- technique-gemm