---
id: technique-pr-vllm-ascend-3151
title: "PR Insight: vllm-project/vllm-ascend #3151"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - layernorm
  - rmsnorm
  - gemma3
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3151"
---

# PR Insight: vllm-project/vllm-ascend #3151

**Title:** [Model] Optimizing gemma3 model's GemmaRMSNorm function

## Overview
This PR optimizes the GemmaRMSNorm function for Gemma3 models, reducing RMS norm time from 531.5us to 105us per decoding operation. The optimization provides approximately 5x performance improvement for layer normalization.

## Technical Significance
Layer normalization is a frequent operation in transformer models. The 5x performance improvement significantly impacts overall inference latency, especially for models like Gemma3 that use RMS normalization extensively. The optimization likely leverages Ascend's vector unit more efficiently or reduces memory access overhead.

## Related
- `kernel-layernorm-ascendc`, `kernel-gemma3-ascendc`, `technique-vector-unit`