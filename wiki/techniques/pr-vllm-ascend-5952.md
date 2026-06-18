---
id: technique-pr-vllm-ascend-5952
title: "PR Insight: vllm-project/vllm-ascend #5952"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek
  - w8a8
  - mlapo
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5952"
---

# PR Insight: vllm-project/vllm-ascend #5952

**Title:** Default enable MLAPO for deepseek W8A8 models

## Overview
This PR defaults to enabling MLAPO (Multi-Head Latent Attention Page Optimization) for DeepSeek W8A8 models on PD disaggregation, including DeepSeekV3-W8A8 and DeepSeek-R1-W8A8. It also enables MLAPO for DeepSeek SFA Attention W8A8 models like DeepSeek-V3.2-W8A8.

## Technical Significance
MLAPO provides performance optimizations for quantized DeepSeek models by optimizing attention computation. Previously, users needed to manually set VLLM_ASCEND_ENABLE_MLAPO=1. This PR enables it by default for W8A8 DeepSeek models, improving performance automatically. Testing on a single A3 node with DeepSeek V3.2-W8A8 shows 19% improvement in throughput on GSM8K-lite when not explicitly enabling MTP or FULL GRAPH.

## Related
- `technique-mla`, `technique-deepseek`, `technique-w8a8`, `technique-attention-optimization`