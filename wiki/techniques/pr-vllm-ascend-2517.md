---
id: technique-pr-vllm-ascend-2517
title: "PR Insight: vllm-project/vllm-ascend #2517"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - typo-fix
  - naming
  - refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2517"
---

# PR Insight: vllm-project/vllm-ascend #2517

**Title:** [Main][Refactor]Change ASCEND_QUATIZATION_METHOD to ASCEND_QUANTIZATION_METHOD

## Overview
This PR fixes a typo where the constant `ASCEND_QUATIZATION_METHOD` should be `ASCEND_QUANTIZATION_METHOD`. The change affects multiple files including `vllm_ascend/platform.py`, `vllm_ascend/quantization/quant_config.py`, and `vllm_ascend/utils.py`.

## Technical Significance
This naming correction fixes a typo that was present throughout the codebase, improving code correctness and maintainability. The proper spelling `ASCEND_QUANTIZATION_METHOD` accurately reflects the constant's purpose and prevents confusion.

## Related
- `technique-quantization`, `technique-code-cleanup`, `technique-naming-correction`