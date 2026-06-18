---
id: technique-pr-vllm-ascend-4420
title: "PR Insight: vllm-project/vllm-ascend #4420"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4420"
---

# PR Insight: vllm-project/vllm-ascend #4420

**Title:** mkdir triton package and move triton files

**Author:** shiyuan680 | **Merged:** 2025-11-26

## Overview
Modifies __init__, casual_conv1d, sigmoid_gating, fla for improved functionality. The changes affect core inference operations and model compatibility.

## Technical Significance
Triton kernels provide flexible, high-performance implementations that can be customized for specific hardware features. Adding new kernels for sampling, gating, and normalization operations expands the optimization surface for vLLM on Ascend.

## Related
- `language-triton`
