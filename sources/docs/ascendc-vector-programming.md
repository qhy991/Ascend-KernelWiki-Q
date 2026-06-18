---
id: doc-ascendc-vector-programming
title: Ascend C Vector Operator Implementation
type: source-doc
architectures:
- ascend910
- ascend910b
- ascend310p
tags:
- ascendc
- vector
- operator
- cann
date: '2026-06-18'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/Ascendcopdevg/atlas_ascendc_10_0033.html
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

# Ascend C Vector Operator Implementation

Official vector-programming workflow for implementing an Ascend C operator. The guide walks through operator analysis, kernel function definition, class-style Init/Process implementation, GM-to-UB movement with DataCopy, vector compute APIs, and queue-based EnQue/DeQue tensor flow.

## Source

- https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/Ascendcopdevg/atlas_ascendc_10_0033.html
