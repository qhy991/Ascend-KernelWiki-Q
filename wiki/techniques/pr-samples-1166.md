---
id: technique-pr-samples-1166
title: "PR Insight: Ascend/samples #1166"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gemm
  - custom-op
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1166"
---

# PR Insight: Ascend/samples #1166

**Title:** fix gemm sample

## Overview
This PR fixes bugs in the GEMM (General Matrix Multiplication) sample implementation, addressing numerical correctness or performance issues in the operator kernel.

## Technical Significance
Ensures the reliability of the GEMM reference implementation, which is fundamental to many deep learning operations. The fix helps developers avoid similar pitfalls when implementing matrix multiplication kernels.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`