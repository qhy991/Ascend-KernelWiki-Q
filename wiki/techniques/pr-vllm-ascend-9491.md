---
id: technique-pr-vllm-ascend-9491
title: "PR Insight: vllm-project/vllm-ascend #9491"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lightning-indexer
  - sparse-flash-attention
  - aclnn
  - ascendc
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9491"
---

# PR Insight: vllm-project/vllm-ascend #9491

**Title:** [Feature][Ops] Add LightningIndexer and SparseFlashAttention ACLNN ops

## Overview
This PR adds two major ACLNN operators: LightningIndexer for efficient index selection and SparseFlashAttention for sparse attention patterns. The implementation includes complete AscendC kernel code for multiple architectures, host-side tiling, torch adapters, and integration with context parallelism.

## Technical Significance
LightningIndexer provides highly optimized index selection critical for sparse attention and MoE routing. SparseFlashAttention enables efficient computation of sparse attention patterns, which is essential for models like DeepSeek V4. Together, these operators significantly improve inference performance for state-of-the-art sparse attention architectures.

## Related
- `kernel-attention`
- `kernel-flash-attention`
- `hw-cube-unit`
- `hw-vector-unit`