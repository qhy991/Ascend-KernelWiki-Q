---
id: code-cann-ops-adv-matmul
title: "CANN Ops Adv \u2014 Matmul Operators"
type: source-code
repo: Ascend/cann-ops-adv
path: src/matmul
url: https://gitee.com/ascend/cann-ops-adv/tree/master/src/matmul
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- matmul
- gemm
- ascendc
- cann
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
- quantization-int8
kernel_types:
- matmul
- gemm
- quant-matmul
languages:
- ascendc
- cpp
---

# CANN Ops Adv — Matmul Operators

Advanced CANN matmul source directory. This path should be mined for standard, quantized, and grouped matmul variants feeding Cube-unit GEMM pages and quant-matmul recipes.

## Code Location

- Repository: `Ascend/cann-ops-adv`
- Path: `src/matmul`
- URL: https://gitee.com/ascend/cann-ops-adv/tree/master/src/matmul


## Fetched Source

// Path src/matmul not found in repo.