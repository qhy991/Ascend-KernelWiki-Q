---
id: technique-pr-sgl-kernel-npu-162
title: "PR Insight: sgl-project/sgl-kernel-npu #162"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - swiglu
  - quantization
  - bugfix
  - activation
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/162"
---

# PR Insight: sgl-project/sgl-kernel-npu #162

**Title:** [bugfix] swiglu quant

## Overview
Fixes a bug in the SwiGLU quantization operator by adding a mask to cover invalid values. This ensures the operator works correctly across all scenarios, particularly handling edge cases in quantized activation computation.

## Technical Significance
The bug fix addresses numerical stability issues in quantized SwiGLU operations, which are critical for maintaining accuracy in quantized MoE inference. The mask prevents invalid value propagation that could occur in certain input scenarios, ensuring robust and accurate quantized activation computation across different expert configurations.

## Related
- `wiki-technique-quantization`
- `wiki-technique-swiglu`
- `wiki-pattern-bugfix`