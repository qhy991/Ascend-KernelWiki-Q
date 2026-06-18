---
id: technique-pr-vllm-ascend-1320
title: "PR Insight: vllm-project/vllm-ascend #1320"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - quantization
  - w4a8
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1320"
---

# PR Insight: vllm-project/vllm-ascend #1320

**Title:** [0.9.1]support deepseek w4a8 quantization

## Overview
This PR adds W4A8 quantization support for DeepSeek models, extending the existing quantization framework to support lower-bit weights for memory-efficient inference.

## Technical Significance
Enables W4A8 quantization for DeepSeek V2 models, reducing memory footprint by approximately 50% compared to FP16 while maintaining accuracy. The implementation updates DeepSeek model files, quantization configuration, and provides multi-card test coverage. This is essential for deploying large DeepSeek models on memory-constrained Ascend NPUs.

## Related
- `technique-w4a8-quantization`
- `kernel-deepseek`