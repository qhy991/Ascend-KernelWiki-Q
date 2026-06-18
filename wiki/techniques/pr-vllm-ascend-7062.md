---
id: technique-pr-vllm-ascend-7062
title: "PR Insight: vllm-project/vllm-ascend #7062"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - glm
  - w8a8
  - modelslim
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7062"
---

# PR Insight: vllm-project/vllm-ascend #7062

**Title:** [Bugfix] Support quant config in glm46v

## Overview
Adds quantization configuration support for GLM-4.6V models using the ModelSlim quantization method. The implementation enables W8A8 quantized weights to be successfully loaded and run on NPU.

## Technical Significance
Enables quantized inference for GLM-4.6V models by adding proper quantization configuration support. This allows users to leverage Ascend NPU capabilities for efficient quantized GLM model inference.

## Related
- `technique-quantization-w8a8`, `technique-glm`, `technique-modelslim`, `technique-quantization-config`