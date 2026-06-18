---
id: technique-pr-catlass-100
title: "PR Insight: Ascend/catlass #100"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - device-layer
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/100"
---

# PR Insight: Ascend/catlass #100

**Title:** 0516 Migrate Device_layer feature to 00_basic_matmul/01_batched_matmul/02_grouped_matmul_slice_m

## Overview
This PR migrates the device-layer feature to basic matmul, batched matmul, and grouped matmul slice-M implementations. It extends device-layer abstraction across multiple matmul variants in catlass.

## Technical Significance
Consistent device-layer abstraction across all matmul variants reduces code duplication and improves maintainability. This enables unified optimization strategies and better integration with the AscendC runtime across different matmul patterns.

## Related
- `kernel-matmul-ascendc`
- `technique-operator-fusion`