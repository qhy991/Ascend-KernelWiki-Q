---
id: technique-pr-vllm-ascend-3147
title: "PR Insight: vllm-project/vllm-ascend #3147"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - glm
  - model-adaptation
  - configuration
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3147"
---

# PR Insight: vllm-project/vllm-ascend #3147

**Title:** [Quant][GLM] Adapt glm quant.

## Overview
This PR adapts quantization support for GLM models by updating quantization configuration. The changes enable proper quantization workflow for GLM model architectures on the Ascend platform.

## Technical Significance
GLM models have specific architectural requirements for quantization. Adapting the quantization configuration ensures that GLM models can benefit from memory and performance optimizations of quantization while maintaining accuracy. This expands the range of supported quantized models on Ascend.

## Related
- `kernel-quantization-ascendc`, `kernel-glm-ascendc`, `pattern-model-adaptation`