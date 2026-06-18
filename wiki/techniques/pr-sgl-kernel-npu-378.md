---
id: technique-pr-sgl-kernel-npu-378
title: "PR Insight: sgl-project/sgl-kernel-npu #378"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gated-norm
  - activation
  - feature-extension
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/378"
---

# PR Insight: sgl-project/sgl-kernel-npu #378

**Title:** Update layernorm_gated.py

## Overview
This PR adds an activation attribute parameter to the layernorm_gated operator, allowing customization of the activation function used in the gated layer normalization computation. The modification enables flexible configuration of activation types for different model requirements.

## Technical Significance
Adding configurable activation functions to gated layer normalization increases operator flexibility, supporting various transformer architectures that use different activation functions (e.g., SiLU, GeLU, Tanh) in their gated normalization layers. This extensibility improves compatibility with diverse model architectures.

## Related
- `kernel-layernorm-gated`, `kernel-normalization`, `technique-activation-optimization`