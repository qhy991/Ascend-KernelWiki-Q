---
id: technique-pr-samples-2678
title: "PR Insight: Ascend/samples #2678"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - numerical-stability
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2678"
---

# PR Insight: Ascend/samples #2678

**Title:** fix tolerance

## Overview
This PR fixes tolerance values in test assertions or numerical comparisons. The adjustment ensures proper numerical accuracy validation for kernel outputs, accounting for floating-point precision characteristics of NPU operations.

## Technical Significance
Proper tolerance settings are critical for numerical validation in kernel testing. Ascend NPUs may produce results with different precision characteristics compared to CPUs or GPUs, requiring appropriate tolerance configurations for accurate correctness validation.

## Related
- `kernel-matmul-ascendc`
- `kernel-elementwise-ascendc`