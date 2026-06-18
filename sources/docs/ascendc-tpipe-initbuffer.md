---
id: doc-ascendc-tpipe-initbuffer
title: Ascend C TPipe InitBuffer API
type: source-doc
architectures:
- ascend910
- ascend910b
- ascend310p
tags:
- ascendc
- api
- memory
- pipeline
date: '2026-06-18'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0110.html
hardware_features:
- unified-buffer
- instruction-queue
techniques:
- pipeline-scheduling
- double-buffering
- workspace-management
confidence: source-reported
---

# Ascend C TPipe InitBuffer API

Official TPipe InitBuffer reference for allocating queue buffers and slicing LocalTensor storage. This source anchors UB budgeting and queue depth decisions for CopyIn/Compute/CopyOut pipelines.

## Source

- https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0110.html
