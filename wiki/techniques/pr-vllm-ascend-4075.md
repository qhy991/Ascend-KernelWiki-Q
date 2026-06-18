---
id: technique-pr-vllm-ascend-4075
title: "PR Insight: vllm-project/vllm-ascend #4075"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - testing
  - e2e-testing
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4075"
---

# PR Insight: vllm-project/vllm-ascend #4075

**Title:** [Test][e2e][LoRA] Add more e2e tests to cover scenarios of LoRA

## Overview
This PR adds comprehensive end-to-end test cases for LoRA (Low-Rank Adaptation) functionality, covering scenarios where LoRA weights are added to q_proj, v_proj, k_proj, o_proj, gate_proj, up_proj, down_proj, embed_tokens and lm_head modules. The tests use Llama-2-7b-hf and Qwen3-0.6B models to validate LoRA correctness across different model architectures and module types.

## Technical Significance
Comprehensive LoRA testing ensures correctness across all modules that can be adapted with LoRA. Testing multiple module types (attention, MLP, embeddings) reveals edge cases in LoRA implementation. E2E tests provide validation of the complete inference pipeline with LoRA enabled, which is critical for production deployments using parameter-efficient fine-tuning.

## Related
- `technique-lora`, `pattern-testing`, `technique-parameter-efficient-finetuning`, `pattern-e2e-testing`