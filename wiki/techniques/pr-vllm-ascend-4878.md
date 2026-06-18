---
id: technique-pr-vllm-ascend-4878
title: "PR Insight: vllm-project/vllm-ascend #4878"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - nz-format
  - weight-transformation
  - transpose
  - quantization
  - refactor
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4878"
---

# PR Insight: vllm-project/vllm-ascend #4878

**Title:** [refactor] refactor weight trans nz and transpose

## Overview
This PR refactors weight NZ format transformation and transpose logic, introducing a 3-option VLLM_ASCEND_ENABLE_NZ environment variable (0=disable, 1=quant-only, 2=enable-as-possible, default=1). The refactor defines NZ support for different quantization/dtype combinations: W4A4 can't support NZ, W4A8/W8A8 trans NZ by default, fp16/bf16 trans NZ only when VLLM_ASCEND_ENABLE_NZ=2.

## Technical Significance
Centralizes and clarifies NZ format handling with configurable options. Handles exceptional cases like MLAPO weights and MLA/SFA's W_UV weights which have special requirements. The default VLLM_ASCEND_ENABLE_NZ=1 means fp16/bf16 weights no longer trans NZ by default.

## Related
- `technique-nz-format`
- `technique-weight-transformation`
- `technique-transpose`
- `kernel-mlapo`
- `kernel-mla`
- `kernel-sfa`