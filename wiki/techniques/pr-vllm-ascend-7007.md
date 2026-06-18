---
id: technique-pr-vllm-ascend-7007
title: "PR Insight: vllm-project/vllm-ascend #7007"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - qwen-omni
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7007"
---

# PR Insight: vllm-project/vllm-ascend #7007

**Title:** [bugfix]Qwen-Omni quantization model_type bugfix

## Overview
Fixes a quantization bug for Qwen-Omni models related to model_type configuration. The fix addresses incorrect model type handling in the quantization configuration.

## Technical Significance
Corrects quantization configuration for Qwen-Omni multimodal models by fixing model_type handling, ensuring proper weight mapping and quantization application. This fix is essential for accurate quantized inference of Qwen-Omni models.

## Related
- `technique-quantization`, `technique-qwen-omni`, `technique-model-config`