---
id: technique-pr-vllm-ascend-3044
title: "PR Insight: vllm-project/vllm-ascend #3044"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - qwen3-next
  - attention-layers
  - model-compatibility
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3044"
---

# PR Insight: vllm-project/vllm-ascend #3044

**Title:** [Bugfix][LoRA] Fix LoRA bug after supporting Qwen3-Next

## Overview
This PR fixes a LoRA compatibility issue introduced by Qwen3-Next support. The issue occurs because LoRA e2e tests use models like ilama-3.2-1B with attention layer names ending with "*.attn" instead of "*.self_attn", which the previous implementation didn't handle correctly.

## Technical Significance
Different model architectures use different naming conventions for attention layers. The fix ensures LoRA works correctly across models with varying attention layer naming patterns, improving compatibility and robustness of the LoRA implementation.

## Related
- `technique-lora`, `kernel-qwen3-next-ascendc`, `pattern-attention-layer-naming`