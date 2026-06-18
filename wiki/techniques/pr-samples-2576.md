---
id: technique-pr-samples-2576
title: "PR Insight: Ascend/samples #2576"
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
  - "https://gitee.com/ascend/samples/pulls/2576"
---

# PR Insight: Ascend/samples #2576

**Title:** 修复Matmul单算子工程多核用例的精度问题

## Overview
This PR fixes precision issues in the matmul operator's multi-core test cases. Multi-core execution on Ascend requires careful synchronization and data partitioning to maintain numerical accuracy.

## Technical Significance
Precision bugs in multi-core scenarios can be subtle and difficult to diagnose. The fix demonstrates correct multi-core programming patterns for matmul on Ascend hardware.

## Related
- `kernel-matmul-ascendc`, `hw-cube-unit`, `pattern-synchronization`