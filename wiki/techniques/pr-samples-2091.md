---
id: technique-pr-samples-2091
title: "PR Insight: Ascend/samples #2091"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - samples
  - elementwise
  - alignment
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2091"
---

# PR Insight: Ascend/samples #2091

**Title:** 提交非对齐Add算子样例

## Overview
This PR contributes a sample implementation of the Add elementwise operator specifically for non-aligned memory access patterns. The example demonstrates how to handle tensors that don't meet alignment requirements for optimal hardware utilization.

## Technical Significance
Non-aligned memory access is common in inference workloads with dynamic shapes. This sample teaches developers how to handle misaligned tensors in AscendC, which impacts Vector unit efficiency and may require padding or special tiling strategies to avoid bank conflicts in the Unified Buffer.

## Related
- `technique-bank-conflict-avoidance`
- `technique-vector-unit`
- `technique-elementwise`