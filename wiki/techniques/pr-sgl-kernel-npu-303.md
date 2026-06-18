---
id: technique-pr-sgl-kernel-npu-303
title: "PR Insight: sgl-project/sgl-kernel-npu #303"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - layout
  - dispatch
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/303"
---

# PR Insight: sgl-project/sgl-kernel-npu #303

**Title:** fix layout numTokensPerExpertTensor partial Initialization bug

## Overview
Fixes incorrect layout calculation results that occur when the number of experts is not a multiple of 8. The bug was caused by misalignment during copying operations, leading to calculation errors.

## Technical Significance
Layout calculation correctness is fundamental for MoE operation accuracy. This fix prevents computational errors that occur with non-standard expert counts, ensuring reliable operation across all possible MoE configurations regardless of expert count divisibility.

## Related
- `wiki-kernel-moe`
- `wiki-technique-layout`
- `wiki-technique-bugfix`
- `wiki-technique-memory-alignment`