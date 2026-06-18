---
id: technique-pr-samples-2227
title: "PR Insight: Ascend/samples #2227"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - reduce
  - reduce-min
  - non-aligned
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2227"
---

# PR Insight: Ascend/samples #2227

**Title:** 添加非对齐ReduceMin自定义算子样例说明

## Overview
This PR adds documentation and sample implementation for a non-aligned ReduceMin custom operator, showing how to find the minimum value across tensors with unaligned memory layouts.

## Technical Significance
Completes the reduction operator coverage with ReduceMin, demonstrating the pattern for min-reduction operations and handling of alignment constraints that are common in practical workloads.

## Related
- `technique-cube-vector-overlap`
- `technique-data-reuse`