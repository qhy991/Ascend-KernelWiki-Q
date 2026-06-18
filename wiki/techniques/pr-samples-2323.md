---
id: technique-pr-samples-2323
title: "PR Insight: Ascend/samples #2323"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - elementwise
  - logarithmic
  - s2-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2323"
---

# PR Insight: Ascend/samples #2323

**Title:** 【S2算子提交】Xlogy算子

## Overview
This PR submits the Xlogy operator as an S2 (level 2) operator sample, providing a reference implementation for the x*log(y) elementwise operation commonly used in machine learning.

## Technical Significance
Adds a reference implementation for the xlogy operation, demonstrating how to efficiently implement this logarithmic elementwise operation on Ascend hardware with proper handling of numerical edge cases.

## Related
- `kernel-elementwise-ascendc`