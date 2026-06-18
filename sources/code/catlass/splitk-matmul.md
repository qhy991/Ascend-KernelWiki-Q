---
id: code-catlass-splitk-matmul
title: CATLASS Split-K Matmul Example
type: source-code
repo: Ascend/catlass
path: examples/09_splitk_matmul
url: https://gitee.com/ascend/catlass/tree/master/examples/09_splitk_matmul
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- split-k
- matmul
- reduction
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- global-memory
- l1-buffer
- l0-buffer
techniques:
- atomic-accumulation
- tiling-strategy
- pipeline-scheduling
kernel_types:
- matmul
- gemm
- reduce
languages:
- cpp
- ascendc
---

# CATLASS Split-K Matmul Example

CATLASS Split-K matmul example showing how K-dimension partitioning and accumulation are represented for GEMM shapes that need more parallelism or better tile balance.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/09_splitk_matmul`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/09_splitk_matmul
