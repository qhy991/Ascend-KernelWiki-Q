---
id: code-sgl-kernel-npu-laser-attention
title: SGL Kernel NPU Laser Attention Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/attentions/csrc/ops/laser_attention
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/laser_attention
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- laser-attention
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
- data-reuse
- pipeline-scheduling
kernel_types:
- attention
- flash-attention
languages:
- cpp
- ascendc
---

# SGL Kernel NPU Laser Attention Operator

SGL Kernel NPU laser attention operator directory anchoring an attention variant with custom host and kernel code for serving workloads.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/attentions/csrc/ops/laser_attention`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/attentions/csrc/ops/laser_attention
