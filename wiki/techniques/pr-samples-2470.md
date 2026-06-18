---
id: technique-pr-samples-2470
title: "PR Insight: Ascend/samples #2470"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - samples
  - pooling
  - reduce
  - a2-adaptation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2470"
---

# PR Insight: Ascend/samples #2470

**Title:** 【32】GlobalAvgPoolSample算子增加对Atlas A2训练系列产品适配

## Overview
This PR adds Atlas A2 training series product adaptation support to the GlobalAvgPoolSample operator, enabling global average pooling operations to run on Atlas A2 hardware.

## Technical Significance
Extends hardware support for the global average pooling sample to Atlas A2 training products, providing developers with reference implementations for reduce operations on the latest Ascend architecture.

## Related
- `kernel-reduce-ascendc`