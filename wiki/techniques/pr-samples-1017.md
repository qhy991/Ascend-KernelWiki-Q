---
id: technique-pr-samples-1017
title: "PR Insight: Ascend/samples #1017"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - vector-unit
  - elementwise
  - api-cleanup
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1017"
---

# PR Insight: Ascend/samples #1017

**Title:** vsub vadd vmul接口整改

## Overview
Refactors and improves the vsub, vadd, and vmul interfaces in the samples codebase. These are vector elementwise operations.

## Technical Significance
Standardizes elementwise vector operations across samples, ensuring consistent API design and implementation patterns. These operations map to vector-unit instructions on Ascend hardware.

## Related
- `kernel-elementwise` / `technique-vector-unit`
