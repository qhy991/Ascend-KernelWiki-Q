---
id: code-catlass-mla
title: CATLASS MLA Example
type: source-code
repo: Ascend/catlass
path: examples/19_mla
url: https://gitee.com/ascend/catlass/tree/master/examples/19_mla
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- mla
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
- matmul
- flash-attention
languages:
- cpp
- ascendc
---

# CATLASS MLA Example

CATLASS MLA example providing code evidence for attention-style matmul pipelines used in inference, including mixed Cube/Vector work and cache-aware data movement.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/19_mla`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/19_mla
