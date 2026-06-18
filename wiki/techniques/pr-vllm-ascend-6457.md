---
id: technique-pr-vllm-ascend-6457
title: "PR Insight: vllm-project/vllm-ascend #6457"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - bugfix
  - inference
  - crash-fix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6457"
---

# PR Insight: vllm-project/vllm-ascend #6457

**Title:** [v0.13.0][Lora][BugFix] Fix crash on base model requests with LoRA enabled

## Overview
This PR fixes a critical bug where requesting the base model would cause the model process to crash when LoRA is enabled. While LoRA module requests worked correctly, base model requests would fail and cause a core dump.

## Technical Significance
Fixes a severe crash issue in the model runner v1 implementation that affects mixed LoRA and base model inference scenarios. The bug caused complete process termination when switching between LoRA and base model requests, making it impossible to serve both types of requests in the same deployment.

## Related
- `technique-lora`