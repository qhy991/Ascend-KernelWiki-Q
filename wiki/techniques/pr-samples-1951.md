---
id: technique-pr-samples-1951
title: "PR Insight: Ascend/samples #1951"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - multi-core
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1951"
---

# PR Insight: Ascend/samples #1951

**Title:** 增加MatMul样例多核运算支持

## Overview
This PR adds multi-core support to the MatMul sample, demonstrating how to partition matrix multiplication work across multiple AICores to improve throughput for large matrix operations.

## Technical Significance
Shows proper multi-core programming patterns on Ascend hardware, including workload partitioning, tiling strategies for parallel execution, and synchronization mechanisms. This is essential for achieving high performance on large matrices.

## Related
- `kernel-matmul-ascendc`
- `technique-nz-tiling`
- `technique-pipeline-scheduling`