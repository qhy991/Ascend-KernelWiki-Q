---
id: code-catlass-group-gemm
title: CATLASS Group GEMM Example
type: source-code
repo: Ascend/catlass
path: examples/16_group_gemm
url: https://gitee.com/ascend/catlass/tree/master/examples/16_group_gemm
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- grouped-gemm
- moe
- cpp
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- nz-format
- l1-buffer
- l0-buffer
techniques:
- nz-tiling
- tiling-strategy
- pipeline-scheduling
kernel_types:
- grouped-gemm
- gemm
- moe
languages:
- cpp
- ascendc
---

# CATLASS Group GEMM Example

CATLASS grouped GEMM example used as code evidence for MoE-style grouped matmul on Ascend. It demonstrates template-based per-group GEMM dispatch and Cube-friendly tile/lifecycle organization.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/16_group_gemm`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/16_group_gemm
