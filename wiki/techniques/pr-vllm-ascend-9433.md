---
id: technique-pr-vllm-ascend-9433
title: "PR Insight: vllm-project/vllm-ascend #9433"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - deepseek-v4
  - cv-parallel
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9433"
---

# PR Insight: vllm-project/vllm-ascend #9433

**Title:** [Attention][Feature] Add mla prolog cv parallel for dsv4

## Overview
This PR adds MLA (Multi-head Latent Attention) prolog compute vector (CV) parallelism support for DeepSeek V4. The implementation updates DSA attention, CV linear operations, DSA operators, and configuration handling to enable parallel MLA prolog computation.

## Technical Significance
CV parallelism for MLA prolog enables efficient distribution of the pre-attention computation across multiple devices, improving scalability for large models. This is particularly important for DeepSeek V4 which uses MLA extensively for memory-efficient attention.

## Related
- `kernel-attention`
- `kernel-mla`
- `technique-hccl-optimization`