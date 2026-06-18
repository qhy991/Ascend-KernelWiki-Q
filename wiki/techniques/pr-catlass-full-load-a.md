---
id: technique-pr-catlass-full-load-a
title: "PR Insight: Catlass Full Load A Strategy"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - memory-optimization
  - matmul
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/201"
---

# PR Insight: Catlass Full Load A Strategy

**Source:** [Catlass PR #201](https://gitee.com/ascend/catlass/pulls/201)

Matrix Multiplication (Matmul) on Ascend NPUs is governed by strict tiling strategies. Because matrices $A$ (Activations) and $B$ (Weights) are typically too large to fit in the L1 Buffer simultaneously, they are tiled into smaller blocks (e.g., $M \times K$ and $K \times N$).

## The Decode Phase Imbalance

During the **Decode phase** of autoregressive LLM generation, the Batch Size is usually very small (e.g., $M=1$ or $M=16$). 
- This means the $A$ matrix (Activations: $M \times K$) is tiny (often just a few kilobytes).
- However, the $B$ matrix (Weights: $K \times N$) remains massive (hundreds of megabytes).

In standard tiling, the NPU might repeatedly fetch small slices of $A$ from Global Memory alongside slices of $B$.

## `matmul_full_loadA` Optimization

This PR introduces the `25_matmul_full_loadA` example, highlighting a specific memory hierarchy optimization.

### Mechanics:
1. **Pinning**: If the $A$ matrix is small enough (which is true during Decode), the Catlass operator loads the *entire* $A$ matrix into the L1 Buffer once.
2. **L1 Residence**: The $A$ matrix is flagged to remain resident in L1. 
3. **Zero MTE Reads for A**: As the massive $B$ matrix streams through the NPU via the Memory Transfer Engine (MTE), it continuously multiplies against the resident $A$ matrix. The MTE never has to issue another read instruction for $A$.

This simple but profound constraint modification completely eliminates the memory bandwidth overhead of the Activations during Vector-Matrix multiplication scenarios.
