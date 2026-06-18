---
id: code-catlass-basic-matmul
title: CATLASS Basic Matmul Example
type: source-code
repo: Ascend/catlass
path: examples/00_basic_matmul
url: https://gitee.com/ascend/catlass/tree/master/examples/00_basic_matmul
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- matmul
- cpp
- ascendc
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- l1-buffer
- l0-buffer
- nz-format
techniques:
- nz-tiling
- pipeline-scheduling
- double-buffering
kernel_types:
- matmul
- gemm
languages:
- cpp
- ascendc
---

# CATLASS Basic Matmul Example

CATLASS basic GEMM example showing the template stack for Cube-unit matmul: architecture tags, operand layouts, L1/L0 tile shapes, block-level MMAD, scheduling, and host-side stream launch.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/00_basic_matmul`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/00_basic_matmul
