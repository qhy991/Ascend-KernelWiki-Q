---
id: technique-pr-vllm-ascend-6648
title: "PR Insight: vllm-project/vllm-ascend #6648"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w4a4
  - laos
  - cleanup
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6648"
---

# PR Insight: vllm-project/vllm-ascend #6648

**Title:** [main][Quant] Remove unused rotation functions and parameters from W4A4 LAOS quantization

## Overview
This PR removes unused rotation-related code from W4A4 LAOS dynamic quantization, including set_rotation_config, apply_rotation methods, and rotation_type field with associated parameters (heads_rotation, kronecker_rotation_n, kronecker_rotation_m).

## Technical Significance
Cleans up dead code in W4A4 LAOS quantization implementation that was never called in the current workflow. The removal simplifies the codebase and reduces maintenance burden without affecting functionality.

## Related
- `technique-quantization`