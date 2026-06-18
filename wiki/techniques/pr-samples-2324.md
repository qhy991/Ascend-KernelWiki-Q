---
id: technique-pr-samples-2324
title: "PR Insight: Ascend/samples #2324"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - activation
  - gelu
  - s2-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2324"
---

# PR Insight: Ascend/samples #2324

**Title:** 【S2算子提交】Gelu算子

## Overview
This PR submits the GELU operator as an S2 (level 2) operator sample, providing a reference implementation for the Gaussian Error Linear Unit activation function used extensively in transformer models.

## Technical Significance
Adds a critical activation function sample for transformer architectures, demonstrating how to efficiently implement GELU on Ascend hardware with proper handling of the complex mathematical computation.

## Related
- `kernel-activation-ascendc`