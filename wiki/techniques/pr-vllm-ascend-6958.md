---
id: technique-pr-vllm-ascend-6958
title: "PR Insight: vllm-project/vllm-ascend #6958"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - accuracy
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6958"
---

# PR Insight: vllm-project/vllm-ascend #6958

**Title:** [bugfix][LoRA] Fix the lora accuracy issue introduced by the upstream vLLM changed.

## Overview
Fixes LoRA end-to-end test accuracy issues caused by upstream vLLM PR #32005. The fix addresses changes in upstream vLLM that affected LoRA behavior in the Ascend implementation.

## Technical Significance
Maintains LoRA accuracy compatibility with upstream vLLM changes by fixing the accuracy regression. This ensures that LoRA fine-tuned models continue to work correctly on Ascend hardware with updated vLLM versions.

## Related
- `technique-lora`, `technique-accuracy`, `technique-upstream-compatibility`