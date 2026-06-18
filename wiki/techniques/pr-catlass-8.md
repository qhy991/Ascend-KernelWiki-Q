---
id: technique-pr-catlass-8
title: "PR Insight: Ascend/catlass #8"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - code-quality
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/8"
---

# PR Insight: Ascend/catlass #8

**Title:** 合并KernelInfo、命名规范

## Overview
This PR consolidates KernelInfo-related code and establishes naming conventions across the catlass repository. It aims to improve code organization and consistency in Ascend matrix multiplication kernel implementations.

## Technical Significance
Naming conventions and consolidated kernel information structures are essential for maintaining large-scale AscendC kernel libraries. This refactoring improves maintainability and reduces cognitive load when working with multiple matmul variants and configurations.

## Related
- `kernel-matmul-ascendc`