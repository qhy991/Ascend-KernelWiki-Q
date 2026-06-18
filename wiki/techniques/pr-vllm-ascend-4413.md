---
id: technique-pr-vllm-ascend-4413
title: "PR Insight: vllm-project/vllm-ascend #4413"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4413"
---

# PR Insight: vllm-project/vllm-ascend #4413

**Title:** [Ops][Triton] Add a triton kernel supporting partial rope.

**Author:** whx-sjtu | **Merged:** 2025-12-02

## Overview
Adds new Triton kernel implementations for Ascend NPU acceleration. The kernels support operations like fused GDN gating, sampling, L2 normalization, and partial rotary embeddings. These custom kernels improve performance for inference workloads by leveraging NPU hardware more efficiently.

## Technical Significance
Triton kernels provide flexible, high-performance implementations that can be customized for specific hardware features. Adding new kernels for sampling, gating, and normalization operations expands the optimization surface for vLLM on Ascend.

## Related
- `language-triton`
