---
id: technique-pr-samples-2274
title: "PR Insight: Ascend/samples #2274"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - less-equal
  - elementwise
  - atlas-a2
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2274"
---

# PR Insight: Ascend/samples #2274

**Title:** 【2】LessEqualSample算子增加对Atlas A2训练系列产品适配——nan

## Overview
This PR updates the LessEqualSample operator to support Atlas A2 training series products. This involves adapting the operator implementation for the new hardware generation.

## Technical Significance
Demonstrates hardware adaptation patterns for supporting new Ascend product lines. The LessEqual operator is a fundamental elementwise comparison operation used in many neural network operations.

## Related
- `kernel-elementwise`
- `wiki-hardware-atlas-a2`