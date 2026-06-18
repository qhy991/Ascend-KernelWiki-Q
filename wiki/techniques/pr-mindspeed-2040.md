---
id: technique-pr-mindspeed-2040
title: "PR Insight: Ascend/MindSpeed #2040"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - tensor-parallel
  - distributed
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2040"
---

# PR Insight: Ascend/MindSpeed #2040

**Title:** refactor：tp2d重构

## Overview
This PR refactors the 2D tensor parallel (TP2D) implementation in MindSpeed. TP2D is an advanced tensor parallelism strategy that partitions tensors across two dimensions to improve scalability for large model training.

## Technical Significance
The 2D tensor parallel refactoring improves the efficiency and maintainability of this critical distributed training feature. TP2D is essential for training very large models on Ascend NPUs, as it reduces communication overhead compared to 1D tensor parallel by optimizing the communication pattern. The refactoring likely improves load balancing, reduces memory footprint, and enhances the integration with pipeline parallel for hybrid parallel strategies. This optimization is particularly important for MoE models and large transformer architectures.

## Related
- `technique-hccl-optimization`
- `technique-cube-vector-overlap`