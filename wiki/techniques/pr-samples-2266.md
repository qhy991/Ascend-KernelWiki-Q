---
id: technique-pr-samples-2266
title: "PR Insight: Ascend/samples #2266"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - scatter
  - elementwise
  - atlas-a2
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2266"
---

# PR Insight: Ascend/samples #2266

**Title:** ScatterSubSample算子增加对Atlas A2训练系列产品适配

## Overview
This PR updates the ScatterSubSample operator to support Atlas A2 training series products, extending hardware compatibility for this scatter operation.

## Technical Significance
Scatter operations are crucial for attention mechanisms, MoE routing, and other index-based operations. Adapting this operator demonstrates hardware-specific optimization patterns for memory access patterns.

## Related
- `kernel-elementwise`
- `technique-bank-conflict-avoidance`