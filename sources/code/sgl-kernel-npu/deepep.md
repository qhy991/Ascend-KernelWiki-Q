---
id: code-sgl-kernel-npu-deepep
title: SGL Kernel NPU DeepEP Operators
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/deepep/ops
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/deepep/ops
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- deepep
- moe
- communication
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- hccs
- global-memory
techniques:
- tensor-parallel-overlap
- hccl-optimization
- pipeline-scheduling
kernel_types:
- moe
- grouped-gemm
- matmul
languages:
- cpp
- ascendc
---

# SGL Kernel NPU DeepEP Operators

SGL Kernel NPU DeepEP operator source, useful as evidence for MoE dispatch/combine kernels and communication-aware inference execution.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/deepep/ops`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/deepep/ops
