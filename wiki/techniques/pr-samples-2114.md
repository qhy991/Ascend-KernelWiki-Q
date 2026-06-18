---
id: technique-pr-samples-2114
title: "PR Insight: Ascend/samples #2114"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - cleanup
  - sample-removal
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2114"
---

# PR Insight: Ascend/samples #2114

**Title:** 删除Addcdiv算子LayerNorm算子MoeSoftMaxTopk算子PreLayerNorm算子

## Overview
This PR removes several operator samples including Addcdiv, LayerNorm, MoeSoftMaxTopK, and PreLayerNorm, likely because they are now provided as built-in operators or the samples are no longer maintained.

## Technical Significance
Simplifies the codebase by removing redundant samples, helping developers focus on current best practices and supported operator patterns. The removal suggests these operations are now well-supported by standard operators.

## Related
- `technique-operator-fusion`