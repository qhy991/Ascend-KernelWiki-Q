---
id: technique-pr-samples-2494
title: "PR Insight: Ascend/samples #2494"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - api
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2494"
---

# PR Insight: Ascend/samples #2494

**Title:** fix matmul api constant bug

## Overview
This PR is a follow-up to the matmul API constant bug fix from PR #2492, likely addressing additional scenarios or improving the fix's comprehensiveness.

## Technical Significance
Iterative fixes indicate the complexity of handling constants correctly across all matmul API usage patterns. Thorough fixes prevent subtle bugs that could lead to incorrect results or performance issues.

## Related
- `kernel-matmul-ascendc`, `pattern-api-usage`