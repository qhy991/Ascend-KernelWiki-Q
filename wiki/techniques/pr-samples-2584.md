---
id: technique-pr-samples-2584
title: "PR Insight: Ascend/samples #2584"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - compilation
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2584"
---

# PR Insight: Ascend/samples #2584

**Title:** 修复Matmul相关用例的编译精度问题

## Overview
This PR continues fixing compilation precision issues in matmul-related test cases, addressing additional scenarios or improving the robustness of previous fixes.

## Technical Significance
Multiple compilation fixes indicate the compiler has several edge cases around matmul compilation. Comprehensive fixes ensure samples work correctly across various matmul configurations and data types.

## Related
- `kernel-matmul-ascendc`, `pattern-compilation`