---
id: code-catlass-block-mmad
title: CATLASS Block MMAD Components
type: source-code
repo: Ascend/catlass
path: include/catlass/gemm/block
url: https://gitee.com/ascend/catlass/tree/master/include/catlass/gemm/block
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- matmul
- template
- cpp
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- l0-buffer
- l1-buffer
techniques:
- pipeline-scheduling
- double-buffering
- tiling-strategy
kernel_types:
- matmul
- gemm
languages:
- cpp
- ascendc
---

# CATLASS Block MMAD Components

CATLASS block-level GEMM component directory. This is the code evidence for how CATLASS decomposes matrix multiplication into reusable MMAD blocks, dispatch policies, and tile-shape abstractions.

## Code Location

- Repository: `Ascend/catlass`
- Path: `include/catlass/gemm/block`
- URL: https://gitee.com/ascend/catlass/tree/master/include/catlass/gemm/block


## Fetched Source

// No source files found in directory.