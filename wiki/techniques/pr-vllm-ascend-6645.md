---
id: technique-pr-vllm-ascend-6645
title: "PR Insight: vllm-project/vllm-ascend #6645"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - auto-detection
  - usability
  - configuration
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6645"
---

# PR Insight: vllm-project/vllm-ascend #6645

**Title:** [Feature][Quant] Auto-detect quantization format from model files

## Overview
This PR adds automatic quantization format detection by inspecting lightweight JSON files (quant_model_description.json, config.json) during engine initialization. The detection checks for ModelSlim ascend format or LLM-Compressor compressed-tensors format, eliminating the need for manual --quantization flags while respecting user-specified overrides.

## Technical Significance
Improves usability by automatically detecting quantization formats without requiring manual configuration. The approach avoids loading heavy safetensors files by inspecting only JSON metadata, making initialization faster while providing flexibility for users who still want explicit control.

## Related
- `technique-quantization`