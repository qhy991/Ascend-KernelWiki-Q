---
id: technique-pr-samples-2463
title: "PR Insight: Ascend/samples #2463"
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
  - "https://gitee.com/ascend/samples/pulls/2463"
---

# PR Insight: Ascend/samples #2463

**Title:** LeakyRelu fix default

## Overview
This PR fixes the default parameter handling in the LeakyRelu sample operator, ensuring correct default behavior for the leaky ReLU activation function.

## Technical Significance
Corrects a parameter initialization issue that could cause incorrect activation outputs when default values were used, improving sample reliability for developers learning activation function implementations.

## Related
- `kernel-activation-ascendc`