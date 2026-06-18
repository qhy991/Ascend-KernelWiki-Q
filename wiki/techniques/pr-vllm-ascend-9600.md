---
id: technique-pr-vllm-ascend-9600
title: "PR Insight: vllm-project/vllm-ascend #9600"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - dequant-swiglu-quant
  - precision
  - bugfix
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9600"
---

# PR Insight: vllm-project/vllm-ascend #9600

**Title:** [Feature] Fix the precision issue of dsV4 caused by dequant_swiglu_quant

## Overview
This PR fixes a precision issue in DeepSeek V4 caused by the dequant_swiglu_quant operation. The changes update the operator definition, kernel implementation, torch bindings, and add E2E tests to validate the fix.

## Technical Significance
Dequantization operations can introduce numerical precision issues that affect model accuracy. Fixing the dequant_swiglu_quant operation ensures that DeepSeek V4 models maintain their expected accuracy when using quantized MoE layers, which is critical for production deployments.

## Related
- `kernel-moe`
- `technique-quantization`
- `hw-cube-unit`