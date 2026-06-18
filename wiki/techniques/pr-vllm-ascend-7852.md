---
id: technique-pr-vllm-ascend-7852
title: "PR Insight: vllm-project/vllm-ascend #7852"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - operator-fusion
  - qwen3vl
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7852"
---

# PR Insight: vllm-project/vllm-ascend #7852

**Title:** [v0.18.0][Feature] support qkv_rmsnorm_mrope for qwen3vl

## Overview
This PR enables the `qkv_rmsnorm_mrope` fusion operator for Qwen3-VL models, which combines QKV projection, RMS normalization, and multi-resolution RoPE (mRoPE) operations into a single kernel. The patch updates the worker initialization and model-specific patches to activate this optimization for both dense and MoE Qwen3-VL variants.

## Technical Significance
Fusing multiple operations into a single kernel reduces memory traffic and kernel launch overhead. The `qkv_rmsnorm_mrope` fusion is particularly important for vision-language models like Qwen3-VL where attention preprocessing involves multiple stages. This optimization improves inference efficiency for Qwen3-VL by reducing the number of separate kernel calls during the attention computation pipeline.

## Related
- `kernel-attention`
- `technique-operator-fusion`
- `kernel-qkv-rmsnorm-mrope`