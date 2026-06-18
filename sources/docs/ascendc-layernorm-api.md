---
id: doc-ascendc-layernorm-api
title: Ascend C LayerNorm High-Level API
type: source-doc
architectures:
- ascend910
- ascend910b
tags:
- ascendc
- layernorm
- operator
- cann
date: '2026-06-18'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0797.html
hardware_features:
- vector-unit
- unified-buffer
- global-memory
techniques:
- tiling-strategy
- data-reuse
confidence: source-reported
---

# Ascend C LayerNorm High-Level API

Official high-level LayerNorm API page. The sample kernel passes GM addresses plus a tiling buffer, uses GET_TILING_DATA, initializes a KernelLayernorm instance, and runs Process(), making it useful evidence for normalization-kernel recipes.

## Source

- https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0797.html
