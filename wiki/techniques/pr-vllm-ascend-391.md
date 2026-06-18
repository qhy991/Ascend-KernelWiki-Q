---
id: technique-pr-vllm-ascend-391
title: "PR Insight: vllm-project/vllm-ascend #391"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8
  - deepseek
  - dynamic
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/391"
---

# PR Insight: vllm-project/vllm-ascend #391

**Title:** feat: add w8a8_dynamic quant & support deepseek quant

## Overview
This PR adds W8A8 dynamic quantization support and enables quantization for DeepSeek models. Implementation includes a 389-line deepseek_v2.py model file, quantization config extensions, and model registration updates.

## Technical Significance
Dynamic W8A8 quantization uses per-token activation quantization instead of static scales, improving accuracy. DeepSeek quantization support enables running compressed DeepSeek models on Ascend, which is critical for deploying these large models efficiently.

## Related
- technique-quantization
- technique-w8a8
- technique-deepseek