---
id: technique-pr-sgl-kernel-npu-109
title: "PR Insight: sgl-project/sgl-kernel-npu #109"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - testing
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/109"
---

# PR Insight: sgl-project/sgl-kernel-npu #109

**Title:** Modify test_low_latency to support int8 quantization testing.

## Overview
This PR updates the low latency test suite to support INT8 quantization testing, enabling validation of quantized MoE operator performance and correctness.

## Technical Significance
Quantization testing is essential for validating that INT8 kernels produce correct results and achieve expected performance gains. The test infrastructure ensures quantized MoE inference can be reliably deployed with accuracy guarantees.

## Related
- `technique-quantization`, `technique-moe`