---
id: technique-pr-samples-2395
title: "PR Insight: Ascend/samples #2395"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - samples
  - elementwise
  - triangular
  - a2-adaptation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2395"
---

# PR Insight: Ascend/samples #2395

**Title:** 【29】TriuSample算子增加对Atlas A2训练系列产品适配 _nan

## Overview
This PR adds Atlas A2 training series product adaptation support to the TriuSample operator, enabling upper triangular matrix operations to run on Atlas A2 hardware.

## Technical Significance
Expands hardware compatibility for the upper triangular operation sample to include Atlas A2 training products, providing reference implementations for elementwise matrix masking operations on the latest Ascend architecture.

## Related
- `kernel-elementwise-ascendc`