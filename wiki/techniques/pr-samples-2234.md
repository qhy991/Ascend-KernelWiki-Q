---
id: technique-pr-samples-2234
title: "PR Insight: Ascend/samples #2234"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - abs
  - duplicate
  - memory-alignment
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2234"
---

# PR Insight: Ascend/samples #2234

**Title:** 添加非对齐的AbsDuplicate用例

## Overview
This PR adds an unaligned use case for the AbsDuplicate operator, demonstrating how to handle absolute value operations with data duplication when memory is not aligned.

## Technical Significance
Shows techniques for combining elementwise operations (abs) with data duplication patterns while handling unaligned memory access. This pattern is useful for broadcasting operations and maintaining layout compatibility.

## Related
- `kernel-elementwise`
- `technique-bank-conflict-avoidance`