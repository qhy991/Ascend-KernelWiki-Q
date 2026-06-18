---
id: code-sgl-kernel-npu-assign-cache
title: SGL Kernel NPU Assign Cache Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/assign_cache_op
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/assign_cache_op
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- kv-cache
- cache
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- vector-unit
- unified-buffer
- global-memory
techniques:
- kv-cache-paging
- data-reuse
- pipeline-scheduling
kernel_types:
- attention
- elementwise
languages:
- cpp
- ascendc
---

# SGL Kernel NPU Assign Cache Operator

SGL Kernel NPU assign-cache operator providing code evidence for KV-cache write and placement logic around attention-serving pipelines.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/assign_cache_op`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/assign_cache_op
