---
id: technique-pr-samples-895
title: "PR Insight: Ascend/samples #895"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - softmax
  - custom-op
  - tik
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/895"
---

# PR Insight: Ascend/samples #895

**Title:** 增加softmax_tik用例

## Overview
This PR adds a TIK-based softmax operator test case, demonstrating how to implement the softmax activation function using TIK interfaces for Ascend hardware acceleration.

## Technical Significance
Provides a reference implementation for softmax, a critical operation in attention mechanisms and classification layers. It shows how to handle exponentiation, reduction, and division operations efficiently on Ascend NPUs.

## Related
- `technique-operator-fusion`
- `technique-cube-vector-overlap`