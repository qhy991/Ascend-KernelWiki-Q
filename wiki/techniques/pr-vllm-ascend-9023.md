---
id: technique-pr-vllm-ascend-9023
title: "PR Insight: vllm-project/vllm-ascend #9023"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - lora
  - qwen3.5
  - gdn
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9023"
---

# PR Insight: vllm-project/vllm-ascend #9023

**Title:** [Feature] Support LoRA with Qwen3.5 dense model.

## Overview
This PR adds support for LoRA (Low-Rank Adaptation) with Qwen3.5 dense models (e.g., Qwen3.5-4B, Qwen3.5-27B). The implementation modifies `AscendGatedDeltaNetAttention` to support the projection layout used in these models and updates LoRA replacement logic in `vllm_ascend/lora/utils.py` to handle merged linear layers with more than two packed modules. The changes align with vLLM's `GatedDeltaNetAttention` implementation.

## Technical Significance
LoRA support for Qwen3.5 dense models enables efficient fine-tuning and deployment of adapters on Ascend NPUs. The fix handles the specific projection layout used by Qwen3.5's GDN attention, ensuring correct weight integration for LoRA adapters. The updated LoRA replacement logic for multi-module packed layers prevents issues with complex layer structures, enabling flexible adapter deployment across different Qwen3.5 model variants.

## Related
- `pattern-lora` (LoRA adapter support)
- `kernel-attention` (GDN attention with LoRA)
- `pattern-qwen3.5` (Qwen3.5 model architecture)