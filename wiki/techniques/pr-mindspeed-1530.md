---
id: technique-pr-mindspeed-1530
title: "PR Insight: Ascend/MindSpeed #1530"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - tp-2d
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1530"
---

# PR Insight: Ascend/MindSpeed #1530

**Title:** tp-2d ulysses-cp-algo bug master

## Overview
This PR fixes a bug in the TP-2D (2D tensor parallelism) algorithm combined with Ulysses and CP (context parallelism). The issue involves the interaction between these parallelism strategies on the master branch.

## Technical Significance
Resolves critical bugs in hybrid parallelism scenarios combining 2D tensor parallelism, Ulysses attention, and context parallelism. These parallelism strategies are essential for training very large models, and correct interaction between them is crucial.

## Related
- `technique-hccl-optimization`
- `kernel-attention`