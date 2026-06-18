---
id: technique-pr-samples-1909
title: "PR Insight: Ascend/samples #1909"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - single-core
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1909"
---

# PR Insight: Ascend/samples #1909

**Title:** 修改Add样例的算子调用方式，添加MatMul单核样例

## Overview
This PR modifies the Add operator sample to use a different kernel invocation pattern and adds a single-core MatMul sample, demonstrating single-AICore execution for smaller workloads.

## Technical Significance
Shows single-core programming patterns which are important for small batch inference or when workloads don't benefit from multi-core parallelization. The updated Add sample also shows improved kernel invocation patterns.

## Related
- `kernel-matmul-ascendc`
- `technique-instruction-queue`