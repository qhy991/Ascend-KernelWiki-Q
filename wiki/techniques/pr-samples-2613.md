---
id: technique-pr-samples-2613
title: "PR Insight: Ascend/samples #2613"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - operator-contrib
  - three-nn
  - cumsum
  - as-strided
  - histogram
  - reduce-sum
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2613"
---

# PR Insight: Ascend/samples #2613

**Title:** 【operator_contrib合入算子】 ThreeNN/Cumsum/AsStrided/Histogram/ReduceSum

## Overview
This PR adds operator_contrib samples for five operators: ThreeNN (3D nearest neighbor), Cumsum (cumulative sum), AsStrided (strided view), Histogram, and ReduceSum. These expand the operator_contrib library with useful patterns.

## Technical Significance
Diverse operator samples demonstrate the flexibility of the operator_contrib framework. Each operator provides a reference implementation for a different computational pattern, from point cloud processing to statistical operations.

## Related
- `technique-custom-operators`, `kernel-reduce`