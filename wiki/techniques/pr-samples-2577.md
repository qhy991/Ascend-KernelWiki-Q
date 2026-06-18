---
id: technique-pr-samples-2577
title: "PR Insight: Ascend/samples #2577"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - multi-core
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2577"
---

# PR Insight: Ascend/samples #2577

**Title:** 修复Matmul单算子工程多核用例的精度问题

## Overview
This PR is a follow-up to the multi-core precision fix from PR #2576, likely addressing additional edge cases or improving the comprehensiveness of the solution.

## Technical Significance
Multiple PRs for multi-core precision indicate the complexity of correctly partitioning and synchronizing matmul across multiple Ascend cores. Thorough fixes ensure reliability for production workloads.

## Related
- `kernel-matmul-ascendc`, `hw-cube-unit`, `pattern-synchronization`