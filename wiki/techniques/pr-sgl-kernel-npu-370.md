---
id: technique-pr-sgl-kernel-npu-370
title: "PR Insight: sgl-project/sgl-kernel-npu #370"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - causal-conv1d
  - bugfix
  - dtype-casting
  - mamba
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/370"
---

# PR Insight: sgl-project/sgl-kernel-npu #370

**Title:** revise causal_conv1d: bugfix and enhance accuracy for model kimilinear

## Overview
This PR fixes a dtype inconsistency bug in the causal_conv1d_update_npu function that caused accuracy degradation in the Kimi-Linear model. The modification ensures proper dtype handling between conv_state and conv_state_update, preventing errors that occurred when types were mismatched.

## Technical Significance
The dtype consistency fix is critical for maintaining numerical accuracy in Mamba-style attention models, particularly for Kimi-Linear which has different dtype requirements than Qwen3-Next models. Without this fix, the operator throws errors or severely degrades precision, highlighting the importance of proper dtype propagation in stateful convolution operations.

## Related
- `kernel-causal-conv1d`, `kernel-mamba`, `technique-dtype-optimization`, `technique-bugfix`