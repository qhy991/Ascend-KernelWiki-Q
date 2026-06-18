---
id: technique-pr-vllm-ascend-6454
title: "PR Insight: vllm-project/vllm-ascend #6454"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - quantization
  - w8a8
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6454"
---

# PR Insight: vllm-project/vllm-ascend #6454

**Title:** [Feat.]: support 310p w8a8

## Overview
This PR introduces W8A8 (8-bit weight, 8-bit activation) static quantization support specifically for the Ascend 310P platform. It adds platform-specific quantization modules, configuration loading, and a dedicated AscendW8A8LinearMethod310P class that handles weight and activation quantization specifics.

## Technical Significance
Enables efficient quantized inference on Ascend 310P hardware by implementing W8A8 static quantization. The platform-specific approach allows the system to dynamically load appropriate quantization configurations (AscendCompressedTensorsConfig, AscendModelSlimConfig) and handle the specifics of weight data manipulation and input parameter broadcasting for the 310P architecture.

## Related
- `technique-quantization`