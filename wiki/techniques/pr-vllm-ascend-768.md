---
id: technique-pr-vllm-ascend-768
title: "PR Insight: vllm-project/vllm-ascend #768"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8
  - bugfix
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/768"
---

# PR Insight: vllm-project/vllm-ascend #768

**Title:** [Bugfix] fix accuracy problem for quantized deepseek models

## Overview
This PR fixes accuracy problems in quantized DeepSeek models caused by NaN (Not a Number) propagation in numerical computations. The solution uses `masked_fill_` to eliminate NaNs without the memory overhead of the `torch.where` approach.

## Technical Significance
NaN propagation is a critical accuracy issue in quantized models. Using `masked_fill_` instead of `torch.where` is more memory-efficient and properly handles NaN elimination during quantized model inference, ensuring numerical stability for DeepSeek W8A8 quantization.

## Related
- `technique-quantization`
- `technique-w8a8`
- `kernel-deepseek`