---
id: technique-pr-samples-2384
title: "PR Insight: Ascend/samples #2384"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - pooling
  - reduce
  - s2-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2384"
---

# PR Insight: Ascend/samples #2384

**Title:** 【S2算子提交】GlobalAvgPool算子

## Overview
This PR submits the GlobalAvgPool operator as an S2 (level 2) operator sample, providing a reference implementation for global average pooling operations on Ascend hardware.

## Technical Significance
Adds a foundational reduce operator sample showing how to implement global average pooling efficiently, demonstrating proper tiling and reduction patterns for this commonly used CNN operation.

## Related
- `kernel-reduce-ascendc`