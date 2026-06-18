---
id: technique-pr-vllm-ascend-9394
title: "PR Insight: vllm-project/vllm-ascend #9394"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - w4a8
  - per-channel
  - gmm
  - swiglu
  - quantization
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9394"
---

# PR Insight: vllm-project/vllm-ascend #9394

**Title:** [Feature][Model] Enable W4A8 per-channel GMM Swiglu quant

## Overview
This PR enables W4A8 per-channel quantization for GMM (Grouped Matrix Multiplication) with SwiGLU activation in MoE models. The implementation updates MoE MLP code, runtime arguments, stage parameters, token dispatchers, and the W4A8 quantization method.

## Technical Significance
Per-channel quantization provides better accuracy than per-tensor quantization by allowing different quantization parameters for each output channel. Enabling this for GMM with SwiGLU improves the accuracy of quantized MoE models while maintaining the memory efficiency benefits of W4A8 quantization.

## Related
- `kernel-moe`
- `technique-quantization`
- `hw-cube-unit`