---
id: technique-pr-samples-2460
title: "PR Insight: Ascend/samples #2460"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - activation
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2460"
---

# PR Insight: Ascend/samples #2460

**Title:** LeakyRelu bug fix

## Overview
This PR fixes a bug in the LeakyRelu sample operator implementation, addressing incorrect computation results in the leaky ReLU activation function.

## Technical Significance
Resolves a computational error that could produce incorrect activation outputs, ensuring the sample accurately demonstrates proper Ascend implementation of the leaky ReLU operation.

## Related
- `kernel-activation-ascendc`