---
id: technique-pr-samples-2077
title: "PR Insight: Ascend/samples #2077"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - samples
  - custom-op
  - scatter
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2077"
---

# PR Insight: Ascend/samples #2077

**Title:** 新增ScatterSub算子自定义实现

## Overview
This PR adds a custom implementation of the ScatterSub operator, which subtracts values into a tensor at specified indices. The sample demonstrates scatter operation patterns for AscendC kernel development.

## Technical Significance
Scatter operations involve non-contiguous memory access patterns that can be challenging on the NPU's Unified Buffer. This sample likely demonstrates strategies for efficient index-based memory updates, possibly using MTE for async transfers and careful access pattern design to avoid bank conflicts.

## Related
- `technique-bank-conflict-avoidance`
- `technique-mte`
- `technique-unified-buffer`