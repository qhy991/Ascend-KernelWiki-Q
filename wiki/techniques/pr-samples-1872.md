---
id: technique-pr-samples-1872
title: "PR Insight: Ascend/samples #1872"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - add
  - elementwise
  - ascendc
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1872"
---

# PR Insight: Ascend/samples #1872

**Title:** 重构AddCustomSample

## Overview
This PR refactors the AddCustomSample to improve code structure, readability, and maintainability. The reorganization likely separates concerns, improves modularity, and applies best practices for AscendC kernel development, making the sample easier to understand and adapt for other custom operators.

## Technical Significance
Code refactoring is important for maintaining high-quality reference implementations. The AddCustomSample is often used as a template for other custom operators, so clean structure and clear patterns help developers create robust AscendC kernels. This refactoring demonstrates best practices for organizing AscendC code on Ascend910/910B.

## Related
- `kernel-elementwise`
- `pattern-code-organization`
- `technique-custom-operator`