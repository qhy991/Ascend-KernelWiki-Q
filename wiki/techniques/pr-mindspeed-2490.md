---
id: technique-pr-mindspeed-2490
title: "PR Insight: Ascend/MindSpeed #2490"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - fb-overlap
  - boundary
  - moe
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2490"
---

# PR Insight: Ascend/MindSpeed #2490

**Title:** 【master】【bugfix】fb-overlap修复边界条件触发gmm无dw报错

## Overview
This PR fixes a boundary condition bug in the FB-overlap (forward-backward overlap) feature that triggered a "GMM no dw" (GMM gradient missing) error. The issue occurred under specific input conditions at the boundaries of tensor dimensions or sequence lengths.

## Technical Significance
Forward-backward overlap is an advanced technique for improving training throughput by overlapping forward and backward computations. Boundary condition bugs can cause rare but critical failures. This fix ensures robust handling of edge cases in the overlap implementation, preventing gradient computation errors.

## Related
- `technique-cube-vector-overlap`
- `kernel-moe`