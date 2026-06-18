---
id: technique-pr-vllm-ascend-3011
title: "PR Insight: vllm-project/vllm-ascend #3011"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - deepseek
  - w4a8
  - per-channel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3011"
---

# PR Insight: vllm-project/vllm-ascend #3011

**Title:** [main][quantization] Support deepseek w4a8 per-channel quantization

## Overview
This PR adds support for DeepSeek W4A8 per-channel quantization, where the MTP layer uses W4A8 per-channel dynamic quantization and other linear layers use W8A8 dynamic quantization. It also adds NZ format weight conversion support for eager mode.

## Technical Significance
Per-channel quantization provides better accuracy than per-tensor quantization, especially for models with varying weight distributions across channels. The NZ format conversion in eager mode improves memory bandwidth utilization. This enables efficient deployment of quantized DeepSeek models on Ascend NPUs.

## Related
- `kernel-quantization-ascendc`, `technique-nz-format`, `kernel-deepseek-ascendc`