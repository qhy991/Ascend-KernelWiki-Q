---
id: technique-pr-vllm-ascend-502
title: "PR Insight: vllm-project/vllm-ascend #502"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - deepseek
  - quantization
  - w8a8
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/502"
---

# PR Insight: vllm-project/vllm-ascend #502

**Title:** [v0.7.3]support MTP in deepseek w8a8 quant model

## Overview
This PR adds MTP (Multi-Token Prediction) support for DeepSeek W8A8 quantized models. Implementation includes a new deepseek_mtp.py file (181 lines) and model registration.

## Technical Significance
Enables speculative decoding with quantized DeepSeek models. Note that the MTP layer remains in BF16 format in current msmodelslim quantization, requiring manual FLOAT quantization_config entries.

## Related
- technique-mtp
- technique-deepseek
- technique-quantization
- technique-w8a8