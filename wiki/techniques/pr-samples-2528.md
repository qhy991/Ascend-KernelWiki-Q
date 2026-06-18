---
id: technique-pr-samples-2528
title: "PR Insight: Ascend/samples #2528"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - mmad
  - matmul
  - bias
  - stride
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2528"
---

# PR Insight: Ascend/samples #2528

**Title:** 修改Mmad样例，cube only bias数据DataCopy stride

## Overview
This PR modifies the Mmad samples to handle bias data DataCopy with correct stride when using cube-only mode. Stride handling is critical when bias tensors are not contiguous or have specific memory layouts.

## Technical Significance
Correct stride handling prevents incorrect bias additions and potential memory corruption. This fix ensures Mmad API samples work correctly with various bias tensor layouts commonly encountered in production.

## Related
- `kernel-matmul-ascendc`, `pattern-api-usage`, `hw-cube-unit`