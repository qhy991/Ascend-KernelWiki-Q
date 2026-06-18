---
id: technique-pr-samples-2217
title: "PR Insight: Ascend/samples #2217"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - add
  - template
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2217"
---

# PR Insight: Ascend/samples #2217

**Title:** 使用三个尖括号调用Add样例，替换核函数调用宏

## Overview
This PR updates the Add operator sample to use three-angle-bracket template syntax for kernel function calls, replacing the previous macro-based invocation approach.

## Technical Significance
Demonstrates the modern AscendC API style using template-based kernel invocation instead of macros. This improves type safety and code readability while maintaining performance.

## Related
- `wiki-language-ascendc`
- `kernel-elementwise`