---
id: technique-pr-samples-2386
title: "PR Insight: Ascend/samples #2386"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - samples
  - elementwise
  - interpolation
  - a2-adaptation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2386"
---

# PR Insight: Ascend/samples #2386

**Title:** 【26】LerpSample算子增加对Atlas A2训练系列产品适配—— nan

## Overview
This PR adds Atlas A2 training series product adaptation support to the LerpSample operator, enabling linear interpolation operations to run on Atlas A2 hardware.

## Technical Significance
Extends hardware support for the linear interpolation operation sample to Atlas A2 training products, providing reference implementations for this common elementwise operation on the latest Ascend architecture.

## Related
- `kernel-elementwise-ascendc`