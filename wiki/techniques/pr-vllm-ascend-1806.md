---
id: technique-pr-vllm-ascend-1806
title: "PR Insight: vllm-project/vllm-ascend #1806"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3
  - quantization
  - fused-ops
  - custom-model
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1806"
---

# PR Insight: vllm-project/vllm-ascend #1806

**Title:** [main] Use AddRmsNormQuant ops in the custom model to optimize Qwen3's performance

## Overview
This PR optimizes Qwen3 quantization model performance by registering a custom model and adding the AddRmsNormQuant operation. This provides a foundation for subsequent performance optimizations based on the custom model structure.

## Technical Significance
Foundation optimization for Qwen3 quantization. The AddRmsNormQuant fused operation combines addition, RMS normalization, and quantization into a single kernel, reducing memory movement and kernel launch overhead critical for quantized inference.

## Related
- `kernel-rmsnorm-ascendc`
- `technique-operator-fusion`
- `technique-quantization`
- `technique-qwen3`