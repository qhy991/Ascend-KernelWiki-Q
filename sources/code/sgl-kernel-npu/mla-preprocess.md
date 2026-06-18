---
id: code-sgl-kernel-npu-mla-preprocess
title: SGL Kernel NPU MLA Preprocess Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/mla_preprocess
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/mla_preprocess
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- mla
- attention
- preprocessing
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
- rope
- elementwise
languages:
- cpp
- ascendc
---

# SGL Kernel NPU MLA Preprocess Operator

SGL Kernel NPU MLA preprocess source directory, anchoring attention preprocessing and cache-shaping code for serving workloads.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/mla_preprocess`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/mla_preprocess
