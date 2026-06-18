---
id: code-sgl-kernel-npu-csrc
title: SGL Kernel NPU Native Source
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- npu
- ascendc
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
- pipeline-scheduling
- online-softmax
- kv-cache-paging
kernel_types:
- attention
- matmul
- softmax
- layernorm
languages:
- cpp
- ascendc
- python
---

# SGL Kernel NPU Native Source

SGLang NPU native source directory. It should be mined for production inference kernels and binding code used by SGLang's Ascend backend.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc
