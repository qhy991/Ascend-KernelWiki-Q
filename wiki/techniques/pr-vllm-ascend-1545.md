---
id: technique-pr-vllm-ascend-1545
title: "PR Insight: vllm-project/vllm-ascend #1545"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - qwen3
  - layernorm
  - fused-ops
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1545"
---

# PR Insight: vllm-project/vllm-ascend #1545

**Title:** [V0.9.1] Use AddRmsNormQuant ops in the custom model to optimize Qwen3's performance

## Overview
This PR uses the fused `AddRmsNormQuant` operator for Qwen3 models, combining addition, RMS normalization, and quantization into a single operation.

## Technical Significance
Optimizes Qwen3 inference by fusing add-RMS-normalize-quantize operations, reducing kernel launch overhead and improving memory locality. The custom operator is particularly beneficial for W8A8 quantized Qwen3 models, improving throughput while maintaining accuracy.

## Related
- `kernel-qwen3`
- `technique-operator-fusion`
- `technique-quantization`