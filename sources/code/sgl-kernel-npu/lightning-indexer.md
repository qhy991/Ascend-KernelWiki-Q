---
id: code-sgl-kernel-npu-lightning-indexer
title: SGL Kernel NPU Lightning Indexer Operator
type: source-code
repo: sgl-project/sgl-kernel-npu
path: csrc/lightning_indexer
url: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/lightning_indexer
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- sglang
- indexing
- attention
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

# SGL Kernel NPU Lightning Indexer Operator

SGL Kernel NPU lightning indexer operator, anchoring code evidence for attention index construction and cache-oriented preprocessing.

## Code Location

- Repository: `sgl-project/sgl-kernel-npu`
- Path: `csrc/lightning_indexer`
- URL: https://github.com/sgl-project/sgl-kernel-npu/tree/main/csrc/lightning_indexer
