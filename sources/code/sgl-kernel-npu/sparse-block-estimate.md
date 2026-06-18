---
id: code-sgl-kernel-npu-sparse-block-estimate
title: SGL Kernel NPU Sparse Block Estimate Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/attentions/csrc/ops/sparse_block_estimate
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/sparse_block_estimate
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- sparse-attention
- block-estimate
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- vector-unit
- unified-buffer
- global-memory
techniques:
- data-reuse
- tiling-strategy
- pipeline-scheduling
kernel_types:
- attention
- reduce
languages:
- cpp
- ascendc
---

# SGL Kernel NPU Sparse Block Estimate Operator

SGL Kernel NPU sparse block estimation source for attention pruning and block selection, useful as evidence for auxiliary attention kernels.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/attentions/csrc/ops/sparse_block_estimate`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/sparse_block_estimate
