---
id: technique-pr-vllm-ascend-3021
title: "PR Insight: vllm-project/vllm-ascend #3021"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - deepseek
  - refactoring
  - model-structure
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3021"
---

# PR Insight: vllm-project/vllm-ascend #3021

**Title:** [3/N][Refactor][Quantization]remove packed_modules_mapping from models

## Overview
This PR moves custom packed_modules_mapping definitions from model files to quant_utils.py, enabling vllm-ascend to maintain the same model classes as the vLLM community. This change allows removal of custom model implementations and improves maintainability.

## Technical Significance
Consolidating packed_modules_mapping reduces code duplication and improves alignment with upstream vLLM. This makes it easier to sync with community changes and reduces the maintenance burden for custom model implementations, particularly for quantized models.

## Related
- `kernel-quantization-ascendc`, `pattern-code-refactoring`, `kernel-deepseek-ascendc`