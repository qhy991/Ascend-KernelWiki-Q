---
id: code-catlass-matmul-add
title: CATLASS Matmul Add Example
type: source-code
repo: Ascend/catlass
path: examples/03_matmul_add
url: https://gitee.com/ascend/catlass/tree/master/examples/03_matmul_add
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- matmul
- epilogue
- fusion
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- l1-buffer
- l0-buffer
techniques:
- cube-vector-overlap
- data-reuse
- pipeline-scheduling
kernel_types:
- matmul
- gemm
- elementwise
languages:
- cpp
- ascendc
---

# CATLASS Matmul Add Example

CATLASS matmul-plus-add example used as code evidence for fused GEMM epilogues, where Cube matmul output is combined with vector-side elementwise work before final storage.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/03_matmul_add`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/03_matmul_add
