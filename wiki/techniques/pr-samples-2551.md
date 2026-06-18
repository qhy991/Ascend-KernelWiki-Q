---
id: technique-pr-samples-2551
title: "PR Insight: Ascend/samples #2551"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - workspace
  - code-quality
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2551"
---

# PR Insight: Ascend/samples #2551

**Title:** matmul 样例修改workspace size硬编码

## Overview
This PR modifies the matmul samples to remove hardcoded workspace sizes. Instead of fixed sizes, the samples now calculate or query the required workspace dynamically.

## Technical Significance
Removing hardcoded workspace sizes improves portability and correctness. Dynamic sizing prevents allocation failures when hardware characteristics or data sizes differ from assumptions.

## Related
- `kernel-matmul-ascendc`, `pattern-api-usage`, `hw-unified-buffer`