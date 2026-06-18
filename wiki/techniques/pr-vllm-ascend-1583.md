---
id: technique-pr-vllm-ascend-1583
title: "PR Insight: vllm-project/vllm-ascend #1583"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - lora
  - einsum
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1583"
---

# PR Insight: vllm-project/vllm-ascend #1583

**Title:** [Bugfix] LoRA logits einsum dimension mismatch in add_lora_logits

## Overview
This PR fixes dimension mismatch in the einsum operation within `add_lora_logits`, ensuring correct LoRA (Low-Rank Adaptation) inference.

## Technical Significance
Corrects LoRA logits computation that produced incorrect outputs due to tensor dimension mismatches. The fix ensures that LoRA adapters produce correct logits when added to base model outputs, maintaining accuracy for fine-tuned models.

## Related
- `technique-lora`
- `technique-einsum`