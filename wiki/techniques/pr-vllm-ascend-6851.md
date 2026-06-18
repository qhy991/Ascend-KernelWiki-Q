---
id: technique-pr-vllm-ascend-6851
title: "PR Insight: vllm-project/vllm-ascend #6851"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - nz-format
  - weight-loading
  - quantization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6851"
---

# PR Insight: vllm-project/vllm-ascend #6851

**Title:** [300I][Bugfix] fix unquant model weight nd2nz error

## Overview
Fixes weight format conversion issues for unquantized models on Ascend 310P by centralizing the logic for converting weights to FRACTAL_NZ format. The refactoring removes platform-specific duplication in `AscendUnquantizedLinearMethod310` and moves the conversion logic to the `maybe_trans_nz` utility function.

## Technical Significance
Ensures correct weight handling for unquantized models on 310P hardware by applying NZ format casts for float16/bfloat16 weights. The centralized approach simplifies code maintenance and prevents platform-specific bugs in weight format conversion.

## Related
- `technique-nz-tiling`, `technique-weight-loading`, `technique-format-conversion`