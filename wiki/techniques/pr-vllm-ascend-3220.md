---
id: technique-pr-vllm-ascend-3220
title: "PR Insight: vllm-project/vllm-ascend #3220"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen-vl
  - quantization
  - configuration
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3220"
---

# PR Insight: vllm-project/vllm-ascend #3220

**Title:** [Bugfix]Fix quant_config input parameter bug in qwenvl series

## Overview
This PR fixes a quantization configuration bug in Qwen-VL series models where non-instantiated variables should be passed as input parameters. The fix corrects the parameter passing to ensure proper quantization configuration.

## Technical Significance
Quantization configuration requires proper parameter instantiation to work correctly. The bug could cause quantization failures or incorrect behavior for Qwen-VL models, which combine vision and language processing. The fix ensures reliable quantization support for multi-modal models.

## Related
- `kernel-quantization-ascendc`, `kernel-qwen3-vl-ascendc`, `pattern-configuration-fix`