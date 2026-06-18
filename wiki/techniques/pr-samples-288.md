---
id: technique-pr-samples-288
title: "PR Insight: Ascend/samples #288"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - conv2d
  - custom-op
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/288"
---

# PR Insight: Ascend/samples #288

**Title:** conv2d and matmul string -> char

## Overview
This PR modifies the conv2d and matmul operator samples to change string parameter handling to character arrays, fixing type compatibility issues with TBE/TIK interfaces that expect C-style strings.

## Technical Significance
Improves cross-platform compatibility and prevents type mismatch errors in custom operator development, particularly important for operator registration and parameter passing in TBE DSL.

## Related
- `kernel-matmul-ascendc`
- `technique-operator-fusion`