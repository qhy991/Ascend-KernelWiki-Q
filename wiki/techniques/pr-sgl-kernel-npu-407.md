---
id: technique-pr-sgl-kernel-npu-407
title: "PR Insight: sgl-project/sgl-kernel-npu #407"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - causal-conv1d
  - mamba
  - state-update
  - performance-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/407"
---

# PR Insight: sgl-project/sgl-kernel-npu #407

**Title:** add kernel conv1d_update

## Overview
This PR adds an AscendC implementation of the conv1d_update kernel for Mamba state updates. The comprehensive implementation includes host-side inference, tiling, kernel code, and stub files for both half and bfloat16 dtypes, with extensive test coverage for validation.

## Technical Significance
Implementing conv1d_update in AscendC provides optimized performance for Mamba-style stateful convolution operations, which are critical for efficient state management in recurrent attention models. The kernel supports both major data types (half and bfloat16) for flexibility across model precision requirements.

## Related
- `kernel-causal-conv1d`, `kernel-mamba`, `kernel-state-update`, `technique-ascendc-implementation`