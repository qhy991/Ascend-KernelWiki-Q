---
id: technique-pr-catlass-201
title: "PR Insight: Ascend/catlass #201"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - data-loading
  - unified-buffer
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/201"
---

# PR Insight: Ascend/catlass #201

**Title:** 新增样例25_matmul_full_loadA，支持A矩阵全载

## Overview
This PR adds example 25 demonstrating matmul with full A matrix loading strategy. It shows how to optimize data movement when the left matrix can be fully loaded into on-chip memory.

## Technical Significance
Full A matrix loading reduces data movement overhead by keeping the left operand in the unified buffer throughout computation. This optimization is beneficial for workloads where the M dimension fits in on-chip memory, enabling better cube unit utilization.

## Related
- `kernel-matmul-ascendc`
- `technique-double-buffering`
- `technique-data-reuse`