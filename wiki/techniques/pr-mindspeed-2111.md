---
id: technique-pr-mindspeed-2111
title: "PR Insight: Ascend/MindSpeed #2111"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - recompute
  - memory
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2111"
---

# PR Insight: Ascend/MindSpeed #2111

**Title:** refactor：recompute func

## Overview
This PR refactors the recompute function implementation in MindSpeed. Recomputation (also known as activation checkpointing) is a memory optimization technique that recomputes activations during backward pass instead of storing them.

## Technical Significance
Recomputation is a critical memory optimization for training large models on Ascend NPUs with limited unified buffer capacity. The refactoring improves the implementation of recompute functions, making them more efficient and easier to maintain. Better recompute implementation reduces memory footprint by trading compute for memory, enabling training of larger models or larger batch sizes. The optimization is particularly important for transformer models with deep architectures and large activation tensors.

## Related
- `technique-data-reuse`
- `technique-nz-tiling`