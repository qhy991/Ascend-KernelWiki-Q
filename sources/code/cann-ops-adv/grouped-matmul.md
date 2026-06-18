---
id: code-cann-ops-adv-grouped-matmul
title: "CANN Ops Adv \u2014 Grouped Matmul"
type: source-code
repo: Ascend/cann-ops-adv
path: src/matmul/grouped_matmul
url: https://gitee.com/ascend/cann-ops-adv/tree/master/src/matmul/grouped_matmul
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- grouped-gemm
- matmul
- moe
- ascendc
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
- matmul
languages:
- ascendc
- cpp
---

# CANN Ops Adv — Grouped Matmul

Advanced grouped matmul operator source. It is code evidence for MoE expert batching, group list handling, and Cube-unit grouped GEMM execution on Ascend.

## Code Location

- Repository: `Ascend/cann-ops-adv`
- Path: `src/matmul/grouped_matmul`
- URL: https://gitee.com/ascend/cann-ops-adv/tree/master/src/matmul/grouped_matmul


## Fetched Source

// Path src/matmul/grouped_matmul not found in repo.