---
id: doc-ascendc-tque
title: Ascend C TQue Memory Queue API
type: source-doc
architectures:
- ascend910
- ascend910b
- ascend310p
tags:
- ascendc
- api
- memory
- queue
date: '2026-06-18'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0137.html
hardware_features:
- unified-buffer
- instruction-queue
- event-sync
techniques:
- pipeline-scheduling
- double-buffering
confidence: source-reported
---

# Ascend C TQue Memory Queue API

Official TQue reference for queue-managed LocalTensor lifetimes. It documents the AllocTensor, EnQue, DeQue, and FreeTensor pattern used to pass tensors between CopyIn, Compute, and CopyOut stages in Ascend C kernels.

## Source

- https://www.hiascend.com/document/detail/en/canncommercial/800/apiref/ascendcopapi/atlasascendc_api_07_0137.html
