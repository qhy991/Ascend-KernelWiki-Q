---
id: technique-pr-samples-1036
title: "PR Insight: Ascend/samples #1036"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - scatter_nd_add
  - operator
  - api-update
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1036"
---

# PR Insight: Ascend/samples #1036

**Title:** scatter_nd_add算子vec接口参数修改

## Overview
This PR modifies parameters for the vector (vec) interface of the scatter_nd_add operator. The change updates the operator's parameter structure or behavior for the vectorized implementation.

## Technical Significance
The scatter_nd_add operator is used for sparse updates in neural networks (e.g., embedding layer updates). Modifying the vector interface parameters may improve performance, fix correctness issues, or align with updated operator specifications. This change affects how developers use the operator in custom kernels on Ascend NPU.

## Related
- Scatter_nd_add operator
- Sparse update operations
- Vectorized interfaces
- Operator parameter handling