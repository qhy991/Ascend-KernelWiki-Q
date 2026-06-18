---
id: technique-pr-vllm-ascend-2797
title: "PR Insight: vllm-project/vllm-ascend #2797"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - code-refactor
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2797"
---

# PR Insight: vllm-project/vllm-ascend #2797

**Title:** [Misc] Move lora patch file into lora module

## Overview
This PR moves LoRA patch files into the dedicated LoRA module and removes unnecessary patching logic, as vLLM Ascend now natively supports the LoRA models that previously required patches. The change reorganizes LoRA-related code into a cleaner module structure.

## Technical Significance
Code cleanup and refactoring to remove redundant LoRA patching infrastructure. Since vLLM now has native LoRA support that covers the previously patched models, this PR removes the custom patch logic and consolidates LoRA operations into a proper module structure, improving maintainability and reducing complexity.

## Related
- `technique-lora`, `technique-code-refactor`, `kernel-attention-ascendc`