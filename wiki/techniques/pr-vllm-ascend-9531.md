---
id: technique-pr-vllm-ascend-9531
title: "PR Insight: vllm-project/vllm-ascend #9531"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - dsa
  - context-parallel
  - distributed
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9531"
---

# PR Insight: vllm-project/vllm-ascend #9531

**Title:** [Feature](dsa, cp): Add DSA context parallel for deepseekv4.

## Overview
This PR adds context parallelism support for DSA (DeepSeek Sparse Attention) in DeepSeek V4. The implementation includes context parallel DSA code, updates to DSA attention, model code for both standard and MTP variants, DSA operators, linear operations, and worker model runners.

## Technical Significance
Context parallelism enables scaling attention computation across multiple devices by partitioning the sequence dimension. Adding this for DSA allows DeepSeek V4 models to leverage context parallelism alongside other parallelism strategies, significantly improving scalability for long-sequence inference.

## Related
- `kernel-attention`
- `technique-hccl-optimization`
- `kernel-flash-attention`