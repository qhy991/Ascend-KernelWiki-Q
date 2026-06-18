---
id: doc-ascendc-tanh-api
title: Ascend C Tanh API
type: source-doc
architectures:
- ascend910
- ascend910b
- ascend310p
tags:
- ascendc
- activation
- api
- cann
date: '2026-06-18'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0489.html
hardware_features:
- vector-unit
- unified-buffer
techniques:
- workspace-management
confidence: source-reported
---

# Ascend C Tanh API

Official high-level Tanh API reference. The API uses LocalTensor operands and a shared temporary buffer allocated through TPipe/TQue, making it evidence for activation kernels that need explicit UB scratch management.

## Source

- https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0489.html
