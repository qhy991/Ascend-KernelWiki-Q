---
id: technique-pr-samples-2554
title: "PR Insight: Ascend/samples #2554"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - quantization
  - code-quality
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2554"
---

# PR Insight: Ascend/samples #2554

**Title:** matmul 常量化用例魔鬼数字修改

## Overview
This PR removes "magic numbers" (hardcoded numerical constants) from the matmul constant quantization samples, replacing them with named constants or computed values. This improves code readability and maintainability.

## Technical Significance
Magic numbers make code difficult to understand and modify. Replacing them with named constants documents the intent and makes it easier to change parameters correctly.

## Related
- `kernel-matmul-ascendc`, `technique-quantization`, `pattern-code-quality`