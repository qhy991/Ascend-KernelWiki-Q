---
id: technique-pr-vllm-ascend-1037
title: "PR Insight: vllm-project/vllm-ascend #1037"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - qwen3
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1037"
---

# PR Insight: vllm-project/vllm-ascend #1037

**Title:** [V0.7.3][LoRA][Qwen3] Make v0.7.3 support Qwen3+LoRA

## Overview
This PR fixes compatibility between vLLM v0.7.3 and Qwen3 models with LoRA adapters by modifying `vllm_ascend/models/qwen3.py`. The issue occurred because vLLM v0.7.3 lacked the upstream PR that added proper support, causing a "Qwen3ForCausalLM object has no attribute 'embedding_modules'" error when launching Qwen3+LoRA models.

## Technical Significance
This PR enables LoRA fine-tuning support for Qwen3 models on Ascend hardware, which is critical for efficient parameter-efficient fine-tuning in production inference scenarios. The fix ensures backward compatibility with v0.7.3 while maintaining the LoRA adapter functionality.

## Related
- `technique-lora`
- `technique-qwen3`