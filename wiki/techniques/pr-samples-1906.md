---
id: technique-pr-samples-1906
title: "PR Insight: Ascend/samples #1906"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - softmax
  - topk
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1906"
---

# PR Insight: Ascend/samples #1906

**Title:** 添加MoeSoftMaxTopK样例

## Overview
This PR adds a MoE (Mixture of Experts) SoftMax TopK operator sample, implementing the expert selection operation used in MoE architectures to select the top-k experts for each token.

## Technical Significance
Provides a reference implementation for MoE expert selection, showing how to efficiently compute SoftMax over expert scores and select top-k experts. This is critical for scaling transformer models with MoE.

## Related
- `technique-operator-fusion`
- `technique-cube-vector-overlap`