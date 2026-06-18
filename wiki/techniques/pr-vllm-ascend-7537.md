---
id: technique-pr-vllm-ascend-7537
title: "PR Insight: vllm-project/vllm-ascend #7537"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v3.2
  - c8-quantization
  - hadamard
  - rotary-embedding
  - precision
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7537"
---

# PR Insight: vllm-project/vllm-ascend #7537

**Title:** [Bugfix]Fix deepseek 3.2 C8  precision by rotary tensor

## Overview
This PR fixes DeepSeek V3.2 C8 quantization precision by properly retrieving the Hadamard matrix from weights during attention quantization. The fix ensures the rotary embedding computation uses correct quantized parameters.

## Technical Significance
This fix matters for DeepSeek V3.2 C8 quantization accuracy. The Hadamard matrix is required for rotary embedding computation in DeepSeek's attention mechanism. Without proper retrieval and quantization of this matrix, precision degradation occurs. The fix ensures correct C8 quantization of both attention weights and the Hadamard matrix.

## Related
- technique-quantization
- technique-c8-quantization
- technique-rotary-embedding