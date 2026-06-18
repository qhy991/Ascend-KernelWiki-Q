---
id: technique-pr-samples-2492
title: "PR Insight: Ascend/samples #2492"
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
  - "https://gitee.com/ascend/samples/pulls/2492"
---

# PR Insight: Ascend/samples #2492

**Title:** fix matmul api constant bug

## Overview
This PR fixes a bug in the matmul API related to handling constant parameters or constant data. The bug likely affected how constant weights or tensors were passed to the matmul operation.

## Technical Significance
Correct handling of constants is critical for performance (constants can be optimized) and correctness (constants must not be modified). This fix ensures matmul samples work correctly with constant inputs.

## Related
- `kernel-matmul-ascendc`, `pattern-api-usage`