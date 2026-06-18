---
id: technique-pr-samples-1899
title: "PR Insight: Ascend/samples #1899"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - layernorm
  - pre-layernorm
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1899"
---

# PR Insight: Ascend/samples #1899

**Title:** 添加PreLayerNorm算子样例

## Overview
This PR adds a PreLayerNorm operator sample, implementing the pre-layer normalization operation used in transformer architectures before residual connections.

## Technical Significance
Provides a reference implementation for PreLayerNorm, showing how to implement mean, variance, and normalization operations efficiently on Ascend hardware. This is essential for transformer-style architectures.

## Related
- `technique-operator-fusion`
- `technique-cube-vector-overlap`