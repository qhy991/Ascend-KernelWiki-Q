---
id: technique-pr-vllm-ascend-1584
title: "PR Insight: vllm-project/vllm-ascend #1584"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - deepseek-r1
  - w8a8
  - mtp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1584"
---

# PR Insight: vllm-project/vllm-ascend #1584

**Title:** [Feature] Enable inference support for Deepseekr1-w8a8-MTP

## Overview
This PR enables inference support for DeepSeek-R1 models with W8A8 quantization and MTP (Multi-Token Prediction).

## Technical Significance
Combines three advanced techniques—DeepSeek-R1 architecture, W8A8 quantization, and MTP spec decode—to enable high-throughput, memory-efficient inference. The implementation updates quantization configuration and model files to support this combination.

## Related
- `kernel-deepseek`
- `technique-w8a8-quantization`
- `technique-mtp`