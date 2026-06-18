---
id: technique-pr-vllm-ascend-585
title: "PR Insight: vllm-project/vllm-ascend #585"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek
  - quantization
  - w8a8
  - mix-parallel
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/585"
---

# PR Insight: vllm-project/vllm-ascend #585

**Title:** support deepseek quant & mix-parallel with graphmode

## Overview
This PR adds W8A8 quantization, mixed parallelism (multi-DP, EP+TP), and graph mode support for DeepSeek models. Changes span attention, models, MoE ops, quantization, caching, and worker components.

## Technical Significance
Enables full-scale DeepSeek deployment with quantization, parallel training, and graph acceleration. Mixed parallelism combines data parallelism with tensor and expert parallelism for optimal resource utilization across NPUs.

## Related
- technique-deepseek
- technique-quantization
- technique-mix-parallel
- technique-aclgraph