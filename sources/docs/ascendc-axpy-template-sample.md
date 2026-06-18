---
id: doc-ascendc-axpy-template-sample
title: Ascend C Axpy Template Sample
type: source-doc
architectures:
- ascend910
- ascend910b
- ascend310p
tags:
- ascendc
- elementwise
- vector
- api
date: '2026-06-18'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0064.html
hardware_features:
- vector-unit
- unified-buffer
- global-memory
- mte
techniques:
- pipeline-scheduling
- data-reuse
confidence: source-reported
---

# Ascend C Axpy Template Sample

Official template sample for triple-operand scalar/vector instructions. It shows a complete KernelAxpy class with GlobalTensor binding, TPipe/TQue buffer setup, CopyIn/Compute/CopyOut stages, DataCopy, Axpy, EnQue/DeQue, and FreeTensor.

## Source

- https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0064.html
