---
id: technique-pr-vllm-ascend-1994
title: "PR Insight: vllm-project/vllm-ascend #1994"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-r1
  - w8a8
  - mtp
  - quantization
  - feature-support
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1994"
---

# PR Insight: vllm-project/vllm-ascend #1994

**Title:** [Feature] Enable inference support for Deepseekr1-w8a8-MTP

## Overview
This PR enables inference support for the DeepSeek-R1-W8A8-MTP model, specifically supporting static quantization of the shared_head in MTP layers. This enables end-to-end quantized inference for this advanced model architecture.

## Technical Significance
Feature enablement for advanced models. DeepSeek-R1-W8A8-MTP combines MTP with W8A8 quantization, requiring careful handling of the shared_head weights in MTP layers to maintain model quality while achieving quantization efficiency.

## Related
- `technique-mtp`
- `technique-w8a8-quantization`
- `technique-deepseek-r1`
- `technique-shared-quantization`