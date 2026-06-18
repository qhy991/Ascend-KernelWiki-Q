---
id: technique-pr-vllm-ascend-2172
title: "PR Insight: vllm-project/vllm-ascend #2172"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w4a8
  - deepseek
  - dynamic-quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2172"
---

# PR Insight: vllm-project/vllm-ascend #2172

**Title:** [main][Feature] Support deepseek w4a8 quantization

## Overview
This PR adds support for DeepSeek-R1 w4a8 quantization using mixed quantization where only MoE layers use w4a8_dynamic quantization. The implementation creates `vllm_ascend/quantization/w4a8_dynamic.py` (284 lines) with the `AscendW4A8DynamicFusedMoEMethod` class and adds comprehensive unit and e2e tests.

## Technical Significance
This enables significant memory savings for DeepSeek models by using w4a8_dynamic quantization for MoE experts while keeping other layers in w8a8. The PR provides detailed documentation on using Modelslim to generate w4a8 weights and instructions for running both eager and graph modes. This mixed quantization approach optimizes the memory/performance trade-off for large MoE models.

## Related
- `technique-quantization-w4a8`, `kernel-fused-moe-ascendc`, `technique-mixed-quantization`, `technique-modelslim-integration`