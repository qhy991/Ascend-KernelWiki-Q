---
id: technique-pr-vllm-ascend-10151
title: "PR Insight: vllm-project/vllm-ascend #10151"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - swiglu
  - dequant
  - clamp
  - quantization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10151"
---

# PR Insight: vllm-project/vllm-ascend #10151

**Title:** [BugFix][v0.20.2rc] Preserve no-group dequant SwiGLU clamp

## Overview
This PR preserves no-group dequant SwiGLU clamp behavior in v0.20.2rc, ensuring that SwiGLU activation clamping is correctly maintained for no-group quantization scenarios.

## Technical Significance
Maintains SwiGLU clamp correctness for no-group dequantization in the release candidate branch. Ensures that activation function behavior remains consistent and correct, preventing numerical issues from incorrect clamping.

## Related
- `kernel-swiglu`, `technique-quantization`, `kernel-dequant`, `pattern-activation`