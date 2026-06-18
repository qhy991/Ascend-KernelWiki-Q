---
id: code-sgl-kernel-npu-cache-location-assign
title: SGL Kernel NPU Cache Location Assign Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/cache_location_assign
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/cache_location_assign
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- kv-cache
- scheduling
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
- tiling-strategy
- pipeline-scheduling
kernel_types:
- attention
- elementwise
languages:
- cpp
- ascendc
---

# SGL Kernel NPU Cache Location Assign Operator

SGL Kernel NPU cache-location assignment operator with tiling metadata, useful for mining serving-side KV-cache placement patterns.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/cache_location_assign`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/cache_location_assign
