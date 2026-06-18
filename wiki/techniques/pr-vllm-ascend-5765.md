---
id: technique-pr-vllm-ascend-5765
title: "PR Insight: vllm-project/vllm-ascend #5765"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - layernorm
  - triton
  - qwen3
  - elementwise
  - normalization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5765"
---

# PR Insight: vllm-project/vllm-ascend #5765

**Title:** [Ops] Add layernorm for qwen3Next

## Overview
This PR adds a specialized layernorm Triton operator for the Qwen3Next model to improve performance. The implementation adds `layernorm_gated.py` with a gated layernorm implementation, updates `layernorm.py` to integrate the new operator, and adds configuration logic in `utils.py` to enable the operator for Qwen3Next models. The operator is designed to handle Qwen3Next's specific layernorm pattern with gating mechanisms.

## Technical Significance
This optimization introduces a custom Triton kernel for Qwen3Next's layernorm operations, providing better performance than the generic implementation. The gated layernorm pattern in Qwen3Next differs from standard layernorm by including gating operations that modify the normalization computation. The custom Triton kernel can exploit Ascend's hardware capabilities more effectively for this specific pattern. The implementation enables better performance by using the specialized operator when detecting Qwen3Next models, while maintaining compatibility with other models that use standard layernorm.

## Related
- `technique-layernorm`, `technique-triton`, `technique-elementwise`, `technique-operator-specialization`