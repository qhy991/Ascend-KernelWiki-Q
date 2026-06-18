---
id: doc-ascendc-matmul-getbatchc
title: Ascend C Matmul GetBatchC API
type: source-doc
architectures:
- ascend910
- ascend910b
tags:
- ascendc
- matmul
- batched
- cann
date: '2026-06-18'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0668.html
hardware_features:
- cube-unit
- l0-buffer
- l1-buffer
techniques:
- tiling-strategy
confidence: source-reported
---

# Ascend C Matmul GetBatchC API

Official Matmul API page for obtaining a batched C matrix slice after IterateNBatch. It is relevant for batched GEMM and grouped computation recipes that need to reason about per-batch C output tiles.

## Source

- https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0668.html
