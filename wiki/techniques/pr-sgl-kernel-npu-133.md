---
id: technique-pr-sgl-kernel-npu-133
title: "PR Insight: sgl-project/sgl-kernel-npu #133"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mla
  - refactor
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/133"
---

# PR Insight: sgl-project/sgl-kernel-npu #133

**Title:** refactor: make hiddenStateDim a class member in MlaTilingData, Follow up closed PR#82

## Overview
This PR refactors the MLA (Multi-head Latent Attention) preprocess host code by making hiddenStateDim a class member variable instead of passing it through function arguments, improving code readability.

## Technical Significance
Refactoring to use class member variables reduces parameter clutter and makes tiling data more cohesive. This is a follow-up to PR #82 and demonstrates iterative code improvement for maintainability in complex attention kernels.

## Related
- `kernel-attention-ascendc`, `technique-mla`