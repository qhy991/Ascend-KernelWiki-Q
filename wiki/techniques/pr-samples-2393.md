---
id: technique-pr-samples-2393
title: "PR Insight: Ascend/samples #2393"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - samples
  - elementwise
  - logarithmic
  - a2-adaptation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2393"
---

# PR Insight: Ascend/samples #2393

**Title:** 【30】XlogySample算子增加对Atlas A2训练系列产品适配——enkilee

## Overview
This PR adds Atlas A2 training series product adaptation support to the XlogySample operator, enabling x*log(y) elementwise operations to run on Atlas A2 hardware.

## Technical Significance
Expands hardware compatibility for the xlogy operation sample to include Atlas A2 training products, providing reference implementations for logarithmic elementwise operations on the latest Ascend architecture.

## Related
- `kernel-elementwise-ascendc`