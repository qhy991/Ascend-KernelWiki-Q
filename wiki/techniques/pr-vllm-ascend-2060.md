---
id: technique-pr-vllm-ascend-2060
title: "PR Insight: vllm-project/vllm-ascend #2060"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - quantization
  - w4a8
  - qwen
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2060"
---

# PR Insight: vllm-project/vllm-ascend #2060

**Title:** [main][Feature] Support Qwen3 W4A8 quantization

## Overview
This PR adds W4A8_DYNAMIC quantization support for linear layers, enabling dense models like Qwen3 to perform inference with 4-bit weights and 8-bit activations. The implementation includes quantization configuration updates and comprehensive testing infrastructure for quantized model serving on Ascend NPU.

## Technical Significance
W4A8 quantization significantly reduces memory footprint and improves throughput for dense models on Ascend NPU. The integration with msmodelslim provides a complete quantization pipeline, while the Ascend-specific optimizations ensure efficient execution of quantized linear operations.

## Related
- `technique-quantization`
- `kernel-linear-w4a8`
- `technique-operator-fusion`
- `technique-data-reuse`