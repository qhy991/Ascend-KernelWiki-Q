---
id: code-sgl-kernel-npu-block-sparse-attention
title: SGL Kernel NPU Block Sparse Attention Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/attentions/csrc/ops/block_sparse_attention
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/block_sparse_attention
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- block-sparse-attention
- attention
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- unified-buffer
- global-memory
techniques:
- online-softmax
- kv-cache-paging
- pipeline-scheduling
kernel_types:
- attention
- paged-attention
- flash-attention
languages:
- cpp
- ascendc
---

# SGL Kernel NPU Block Sparse Attention Operator

SGL Kernel NPU block sparse attention implementation, providing production-style evidence for sparse attention tiling and cache-aware inference kernels.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/attentions/csrc/ops/block_sparse_attention`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/block_sparse_attention
