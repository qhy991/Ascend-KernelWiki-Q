---
id: technique-fused-rope-mqa-optim
title: "Vectorized Triton Optimizations for Fused RoPE MQA"
type: wiki-technique
architectures:
  - ascend910b
kernel_types:
  - rope
tags:
  - fusion
  - glm5
sources:
  - pr-sgl-kernel-npu-557
confidence: verified
---

# Vectorized Triton Optimizations for Fused RoPE MQA

## Overview
When applying Rotary Position Embeddings (RoPE) in a Multi-Query Attention (MQA) setting, the Query matrix has multiple heads (`Hq`) while the Key matrix typically has fewer. A naive implementation loops through each head to compute RoPE, resulting in suboptimal vector utilization.

## Optimization Strategy
1. **Shared Trigonometry Loading**: Cosine and sine embeddings are loaded precisely once per sequence position (`pid_t`).
2. **Vectorized Head Loading**: Rather than indexing elements head-by-head using a loop, the Q matrix block is loaded simultaneously using multi-dimensional array slicing: `head_offs[:, None]`.

## Benefits
- Drastically reduces memory transactions for the `cos` and `sin` tables.
- Allows the compiler to issue wider vectorized loads (`LDG`) instead of multiple narrow transactions, maximizing bandwidth utilization on Ascend architectures.
