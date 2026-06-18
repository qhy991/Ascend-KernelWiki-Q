---
id: technique-pr-vllm-ascend-478
title: "PR Insight: vllm-project/vllm-ascend #478"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - deepseek
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/478"
---

# PR Insight: vllm-project/vllm-ascend #478

**Title:** [quant][bugfix] fix deepseek quant bug

## Overview
This PR fixes a DeepSeek quantization bug by moving scale/offset tensor flattening from model-specific code to the quantization framework (related to #465). Changes remove 108 lines from deepseek_v2.py.

## Technical Significance
Centralizes quantization weight processing logic, making it applicable across models instead of DeepSeek-specific. This improves maintainability and ensures consistent handling of msmodelslim-generated quantized models.

## Related
- technique-quantization
- technique-deepseek