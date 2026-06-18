---
id: technique-pr-vllm-ascend-4119
title: "PR Insight: vllm-project/vllm-ascend #4119"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - causal-conv1d
  - mamba
  - custom-ops
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4119"
---

# PR Insight: vllm-project/vllm-ascend #4119

**Title:** [OPS] support triton causal_conv1d_fn ops

## Overview
This PR adds support for Triton causal_conv1d_fn operators, which are used in Mamba and other state-space models. The implementation includes the Triton kernel and integration with vLLM's triton patching system, enabling efficient 1D causal convolution operations on Ascend NPUs.

## Technical Significance
Causal convolution is a core operation in state-space models like Mamba. Triton kernels provide flexible, high-performance implementation that can be optimized for specific hardware patterns. Supporting this operator enables vLLM Ascend to run Mamba and related models efficiently, expanding the range of supported architectures beyond standard transformers.

## Related
- `technique-triton`, `technique-mamba`, `pattern-custom-ops`, `technique-state-space-models`