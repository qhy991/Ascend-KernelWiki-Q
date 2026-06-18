---
id: technique-pr-vllm-ascend-10011
title: "PR Insight: vllm-project/vllm-ascend #10011"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mlp
  - swiglu
  - quantization
  - triton
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10011"
---

# PR Insight: vllm-project/vllm-ascend #10011

**Title:** [Ops] [BugFix] add swiglu_limit in unquant_apply_mlp

## Overview
This PR adds swiglu_limit parameter handling in unquant_apply_mlp operation, fixing issues with SwiGLU activation function handling in unquantized MLP layers.

## Technical Significance
Fixes SwiGLU activation handling in unquantized MLP layers by adding proper swiglu_limit support. Ensures correct behavior of SwiGLU activation when applying unquantized MLP operations, preventing numerical issues or incorrect activations.

## Related
- `kernel-mlp`, `kernel-swiglu`, `technique-activation`