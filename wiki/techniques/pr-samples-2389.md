---
id: technique-pr-samples-2389
title: "PR Insight: Ascend/samples #2389"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - samples
  - activation
  - gelu
  - a2-adaptation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2389"
---

# PR Insight: Ascend/samples #2389

**Title:** 【28】GeluSample算子增加对Atlas A2训练系列产品适配——Guangyao

## Overview
This PR adds Atlas A2 training series product adaptation support to the GeluSample operator, enabling GELU activation operations to run on Atlas A2 hardware.

## Technical Significance
Extends hardware support for the GELU activation sample to Atlas A2 training products, providing developers with reference implementations for this critical transformer activation function on the latest Ascend architecture.

## Related
- `kernel-activation-ascendc`