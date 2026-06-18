---
id: technique-pr-vllm-ascend-7737
title: "PR Insight: vllm-project/vllm-ascend #7737"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - performance
  - deepseek-ocr2
  - rel-pos-attention
  - custom-decoder
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7737"
---

# PR Insight: vllm-project/vllm-ascend #7737

**Title:** [Performance]Optimize DeepSeekOCR2 RelPosAttention and CustomQwen2Decoder

## Overview
This PR optimizes DeepSeekOCR2 relative position attention and custom Qwen2 decoder performance. The changes affect relative position attention implementation, worker patching, and utility functions.

## Technical Significance
Improves inference performance for DeepSeekOCR2 models by optimizing relative position attention computation and custom decoder logic, reducing latency in vision-language workloads.

## Related
- `kernel-attention`, `pattern-deepseek-architecture`, `technique-custom-decoder`, `pattern-vision-language`, `technique-position-encoding`