---
id: technique-pr-vllm-ascend-6670
title: "PR Insight: vllm-project/vllm-ascend #6670"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - quantization
  - mxfp8
  - qwen
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6670"
---

# PR Insight: vllm-project/vllm-ascend #6670

**Title:** add mxfp8 moe quantization

## Overview
This PR adds MXFP8 quantization support for Qwen MoE models. It implements hardware-specific adaptors for clearer behavior, adds MXFP8 quantization methods, and updates MoE communication, MLP, and token dispatch components to support the new format.

## Technical Significance
Enables MXFP8 quantized MoE inference on Ascend hardware, providing improved memory efficiency while maintaining accuracy. The adaptor pattern improves maintainability by separating hardware-specific quantization behaviors.

## Related
- `kernel-moe`
- `technique-quantization`