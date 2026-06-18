---
id: technique-pr-vllm-ascend-1910
title: "PR Insight: vllm-project/vllm-ascend #1910"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - w4a8
  - moe
  - mlp-decode
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1910"
---

# PR Insight: vllm-project/vllm-ascend #1910

**Title:** [0.9.1][bugfix] W4A8 does not currently support apply_mlp_decode

## Overview
This PR documents and addresses a limitation where W4A8 quantization does not currently support the apply_mlp_decode operation. The fix either implements support or adds proper fallback handling.

## Technical Significance
Feature completeness for W4A8 quantization. The apply_mlp_decode operation is critical for quantized MLP execution, and supporting it in W4A8 mode is necessary for end-to-end quantized inference.

## Related
- `technique-quantization`
- `technique-w4a8`
- `technique-mlp-decode`