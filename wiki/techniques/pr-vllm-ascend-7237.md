---
id: technique-pr-vllm-ascend-7237
title: "PR Insight: vllm-project/vllm-ascend #7237"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - reversion
  - accuracy
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7237"
---

# PR Insight: vllm-project/vllm-ascend #7237

**Title:** Revert "Refactor quantization layer name mapping to leverage vLLM built-in mappers"

## Overview
This PR reverts commit 7ed9e9de which broke Kimi-K2.5 and Qwen-OMN models. The reversion restores the previous quantization layer name mapping implementation to maintain accuracy compatibility with these specific model families.

## Technical Significance
This reversion matters for Ascend quantization accuracy. The original refactoring attempted to leverage vLLM's built-in quantization layer mappers but introduced compatibility issues with certain model architectures. By reverting to the custom mapping, it ensures correct weight loading and quantization behavior for Kimi-K2.5 and Qwen-OMN models on Ascend hardware.

## Related
- technique-quantization