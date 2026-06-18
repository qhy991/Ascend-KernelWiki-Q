---
id: technique-pr-vllm-ascend-893
title: "PR Insight: vllm-project/vllm-ascend #893"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - v1-engine
  - fine-tuning
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/893"
---

# PR Insight: vllm-project/vllm-ascend #893

**Title:** [V1][LoRA][Test] V1 Engine LoRA support & e2e test

## Overview
This PR adds LoRA (Low-Rank Adaptation) support to the V1 engine along with comprehensive end-to-end tests for both single-card and multi-card scenarios. The implementation enables efficient fine-tuning and inference with LoRA adapters.

## Technical Significance
LoRA enables efficient model adaptation without full retraining. Adding LoRA support to the V1 engine allows users to leverage both the improved V1 architecture and LoRA's parameter-efficient fine-tuning benefits, making it practical to deploy multiple fine-tuned variants of base models on Ascend hardware.

## Related
- `technique-lora`
- `kernel-fine-tuning`
- `kernel-inference`