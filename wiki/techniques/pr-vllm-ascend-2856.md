---
id: technique-pr-vllm-ascend-2856
title: "PR Insight: vllm-project/vllm-ascend #2856"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - layernorm
  - quantization
  - modelslim
  - custom-op
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2856"
---

# PR Insight: vllm-project/vllm-ascend #2856

**Title:** [Quantization] register AscendQuantRMSNorm for quantization

## Overview
This PR registers a custom AscendQuantRMSNorm operator to handle the self.bias parameter that ModelSlim generates during quantization, as the standard vLLM RMSNorm implementation does not support this parameter.

## Technical Significance
Enables quantized inference with ModelSlim by providing a custom RMSNorm variant that supports the bias parameter generated during quantization. This is critical for achieving optimal performance with quantized models while maintaining correctness. Custom operator registration allows for seamless integration with vLLM's operator framework.

## Related
- `kernel-layernorm`, `technique-quantization`, `technique-custom-op`