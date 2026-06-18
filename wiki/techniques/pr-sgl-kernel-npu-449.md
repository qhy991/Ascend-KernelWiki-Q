---
id: technique-pr-sgl-kernel-npu-449
title: "PR Insight: sgl-project/sgl-kernel-npu #449"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - causal-conv1d
  - mamba
  - activation
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/449"
---

# PR Insight: sgl-project/sgl-kernel-npu #449

**Title:** bugfix: Add activation setting to torch_causal_conv1d_update_npu

## Overview
This PR fixes a bug where torch_causal_conv1d_update_npu hardcoded SiLU activation and ignored the activation parameter passed by Lfm2MoeShortConv in LFM2-MoE models. The fix adds proper activation handling to respect the parameter value, improving accuracy for models that don't use SiLU.

## Technical Significance
Proper activation function handling is essential for model correctness, particularly for MoE architectures like LFM2-MoE that may use different activation functions. The fix ensures that the kernel respects the intended activation function rather than unconditionally applying SiLU, maintaining model accuracy and flexibility.

## Related
- `kernel-causal-conv1d`, `kernel-mamba`, `kernel-lfm2-moe`, `technique-bugfix`