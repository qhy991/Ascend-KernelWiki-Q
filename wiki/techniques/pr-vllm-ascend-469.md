---
id: technique-pr-vllm-ascend-469
title: "PR Insight: vllm-project/vllm-ascend #469"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - deepseek
  - w8a8
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/469"
---

# PR Insight: vllm-project/vllm-ascend #469

**Title:** [deepseek][bugfix] support deepseek quant

## Overview
This PR adds DeepSeek quantization support and W8A8 dynamic quantization. Implementation includes a 390-line deepseek_v2.py model file and quantization config extensions.

## Technical Significance
Enables quantized DeepSeek models on Ascend, critical for deploying these large models efficiently. W8A8 dynamic quantization improves accuracy compared to static quantization by computing scales per-token.

## Related
- technique-quantization
- technique-w8a8
- technique-deepseek