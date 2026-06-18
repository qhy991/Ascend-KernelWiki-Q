---
id: technique-pr-samples-1275
title: "PR Insight: Ascend/samples #1275"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - slice
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1275"
---

# PR Insight: Ascend/samples #1275

**Title:** 新增slice算子样例

## Overview
This PR adds sample code for the slice operator to the repository. Slice is a tensor manipulation operation that extracts subsets of data along specified dimensions.

## Technical Significance
The slice operator is fundamental in many deep learning workloads, particularly for attention mechanisms and tensor slicing operations. On Ascend hardware, efficient slice implementation requires careful handling of memory strides and potentially format conversions between ND and NZ formats to optimize memory access patterns.

## Related
- kernel-elementwise
- hw-nd-format
- hw-nz-format
- technique-format-conversion