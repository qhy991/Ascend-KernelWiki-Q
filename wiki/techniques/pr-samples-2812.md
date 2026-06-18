---
id: technique-pr-samples-2812
title: "PR Insight: Ascend/samples #2812"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2812"
---

# PR Insight: Ascend/samples #2812

**Title:** add scatter sample * add scatter sample

## Overview
This PR adds scatter operation samples to the repository. The scatter operation is a fundamental tensor manipulation primitive that distributes elements from a source tensor to a destination tensor based on indices.

## Technical Significance
Scatter operations are important for sparse tensor operations, attention mechanisms, and embedding lookups. Adding samples helps developers understand how to implement scatter efficiently on Ascend hardware using AscendC.

## Related
- `pattern-sparse-operations`, `pattern-attention-mechanisms`