---
id: technique-pr-vllm-ascend-7156
title: "PR Insight: vllm-project/vllm-ascend #7156"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - qwen
  - reranker
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7156"
---

# PR Insight: vllm-project/vllm-ascend #7156

**Title:** [Bugfix][LoRA] Fix the bug when runs Qwen3-Reranker-0.6B with LoRA.

## Overview
Fixes initialization errors when running Qwen3-Reranker-0.6B models with `--enable-lora`. The fix addresses specific compatibility issues between Qwen3-Reranker models and LoRA functionality on Ascend hardware.

## Technical Significance
Enables LoRA fine-tuning support for Qwen3-Reranker models by fixing initialization issues. The addition of test cases ensures the fix maintains correctness for this specific model architecture with LoRA enabled.

## Related
- `technique-lora`, `technique-qwen`, `technique-reranker`, `technique-model-initialization`