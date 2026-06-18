---
id: technique-pr-samples-1604
title: "PR Insight: Ascend/samples #1604"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - softmax
  - custom-op
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1604"
---

# PR Insight: Ascend/samples #1604

**Title:** 添加Softmax样例

## Overview
This PR adds a Softmax operator sample implemented in AscendC, demonstrating how to implement this essential activation function efficiently on Ascend hardware.

## Technical Significance
Provides a reference implementation for Softmax in AscendC, showing how to handle the exponential and normalization operations efficiently. Softmax is critical for attention mechanisms and classification layers in transformers.

## Related
- `technique-operator-fusion`
- `technique-cube-vector-overlap`