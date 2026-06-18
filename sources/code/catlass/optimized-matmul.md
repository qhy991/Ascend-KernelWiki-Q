---
id: code-catlass-optimized-matmul
title: CATLASS Optimized Matmul Example
type: source-code
repo: Ascend/catlass
path: examples/06_optimized_matmul
url: https://gitee.com/ascend/catlass/tree/master/examples/06_optimized_matmul
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- optimized-gemm
- matmul
- ascendc
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- l1-buffer
- l0-buffer
- unified-buffer
techniques:
- pipeline-scheduling
- double-buffering
- data-reuse
kernel_types:
- matmul
- gemm
languages:
- cpp
- ascendc
---

# CATLASS Optimized Matmul Example

CATLASS optimized matmul example anchoring higher-performance GEMM variants with explicit scheduling, tile reuse, and buffered movement around Cube computation.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/06_optimized_matmul`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/06_optimized_matmul
