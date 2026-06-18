---
id: technique-pr-samples-2020
title: "PR Insight: Ascend/samples #2020"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - samples
  - elementwise
  - broadcast
  - custom-op
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2020"
---

# PR Insight: Ascend/samples #2020

**Title:** 新增BroadcastCustomSample样例

## Overview
This PR adds a new sample implementation of the Broadcast custom operator. The sample demonstrates how to implement broadcast operations using AscendC, expanding tensor dimensions for elementwise arithmetic across tensors of different shapes.

## Technical Significance
Broadcast operations are fundamental to deep learning frameworks. This sample teaches developers how to handle shape broadcasting logic efficiently on the Vector unit, addressing memory layout considerations and access pattern optimization for various tensor dimension combinations.

## Related
- `technique-elementwise`
- `technique-vector-unit`
- `technique-unified-buffer`